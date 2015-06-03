"""
Author: Jared Mackey
Built to get data from BigOven's API and load it into the database for the recipe organizer.
API Key removed for security.
The API has a request limit of 100 per hour. So time.sleep() is called to slow down the script
 to a manageable pace.
"""

import datetime
import urllib
import time
import base64
import json
import unicodedata
import requests
import yaml

# Script will stop at 100 recipes.
added = 0

search_terms = ["Casserole", "Dessert", "Burger", "Steak", "Lasagna", "Barbecue"]

existing_recipes = yaml.load(requests.get('http://recipes.mackeydevelopments.com/api/recipes/').content)
# existing_recipes = yaml.load(requests.get('http://localhost:8001/recipes/').content)

##################################################
#
# Existing recipe section. This will get all my
# existing recipes and add them to a list by name.
# This is an attempt to prevent duplicates.
#
##################################################
existing_recipes_names = []
existing_recipes_original_ids = []

for recipe in existing_recipes:
    existing_recipes_names.append(recipe["name"].lower())
    existing_recipes_original_ids.append(recipe["original_id"])

# Setting up the variables used in the request to the API
# Please don't use my API key, you can get your own for free from API.bigoven.com
api_key = 'dvxPqd8bsbn6I30J6pqaEMQOOBiysM8M'
headers = {'Accept': 'application/json'}


##################################################
# MAIN LOOP
# This will loop through all of the search terms
#  and run the inner loops.
##################################################
for search_term in search_terms:
    # Default starting page. Change this as needed.
    page = 40
    ##################################################
    # PAGE LOOP
    # This will change the page we are downloading from the API
    # until 100 recipes of this category are added.
    ##################################################
    while added < 100:
        data = requests.get(
            'http://api.bigoven.com/recipes?pg=' + str(page) + '&rpp=50&title_kw=' + search_term + '&api_key=' + api_key,
            headers=headers).content

        data = yaml.load(data.replace("\/", ""))
        if data['Results'] is []:
            break

        for recipeInPage in data['Results']:
            ##################################################
            # RECIPE LOOP
            # Loops through each recipe on the page checking data and then
            #  adding to our API
            ##################################################

            # Checking to see if recipe is already live on the site, if so it just skips it.
            if recipeInPage["Title"].lower() not in existing_recipes_names and\
                            recipeInPage["RecipeID"] not in existing_recipes_original_ids:

                if recipeInPage["HeroPhotoUrl"] != "http://images.bigoven.com/image/upload/recipe-no-image.jpg" and \
                                recipeInPage["HeroPhotoUrl"] != "http://media.bigoven.com/pics/recipe-no-image.jpg" and \
                                recipeInPage["HeroPhotoUrl"] != "http://redirect.bigoven.com/pics/recipe-no-image.jpg" and \
                                recipeInPage["HeroPhotoUrl"] != "http://mda.bigoven.com/pics/recipe-no-image.jpg":
                    if recipeInPage["StarRating"] > 0:
                        print recipeInPage["HeroPhotoUrl"]
                        recipeID = recipeInPage["RecipeID"]

                        ###########################################
                        #
                        # Recipe details is requested from the API
                        #
                        ###########################################

                        recipeContent = requests.get('http://api.bigoven.com/recipe/' + str(recipeID) + '/'
                                                     + "?api_key=" + api_key, headers=headers).content
                        recipe = {
                            'ingredients': [],
                            'original_id': recipeID,
                            'category': search_term,
                        }

                        try:
                            dataFromRecipe = yaml.load(recipeContent.replace("\/", ""))
                            recipe["photo"] = base64.b64encode(urllib.urlopen(dataFromRecipe["HeroPhotoUrl"]).read())
                        except Exception:
                            print "Invalid characters in recipe. Skipping."
                            time.sleep(50)
                            continue

                        # recipe["thumbnail"] = recipe["photo"]
                        recipe["name"] = dataFromRecipe["Title"]
                        recipe["rating"] = dataFromRecipe["StarRating"]

                        # Setting default description
                        if dataFromRecipe["Description"] is "":
                            recipe["description"] = dataFromRecipe["Title"]
                        elif dataFromRecipe["Description"] == "We hope you are enjoying this free experimental developer key at api.bigoven.com.  Production usage of the BigOven API requires a paid plan, which helps offset BigOven's considerable hosting costs.  This message will not appear on any paid plan; visit your developer console at http://api.bigoven.com to purchase an upgraded key. Thank you!":
                            continue
                        else:
                            recipe["description"] = dataFromRecipe["Description"]

                        if dataFromRecipe["Instructions"] == "We hope you are enjoying this free experimental developer key at api.bigoven.com.  Production usage of the BigOven API requires a paid plan, which helps offset BigOven's considerable hosting costs.  This message will not appear on any paid plan; visit your developer console at http://api.bigoven.com to purchase an upgraded key. Thank you!":
                            continue
                        recipe["directions"] = dataFromRecipe["Instructions"]

                        # Building ingredient list from data received from API.
                        for ingredient in dataFromRecipe['Ingredients']:
                            # I thought it was broken becuase of the unicode strings. But figured out aftwards
                            # those are normal in JSON.
                            ingred = {}

                            # Ingred name
                            if type(ingredient["Name"]) is unicode:
                                ingred["name"] = unicodedata.normalize('NFKD', ingredient["Name"]).encode('ascii', 'ignore')
                            else:
                                ingred["name"] = ingredient["Name"]

                            # Ingred quantity
                            if type(ingredient["DisplayQuantity"]) is unicode:
                                ingred["quantity"] = unicodedata.normalize('NFKD', ingredient["DisplayQuantity"]).encode('ascii',
                                                                                                                         'ignore')
                            else:
                                if ingredient["DisplayQuantity"] is "" or ingredient["DisplayQuantity"] is None:
                                    ingred["quantity"] = "Not specified"
                                else:
                                    ingred["quantity"] = ingredient["DisplayQuantity"]

                            # Ingred measurement
                            if type(ingredient["Unit"]) is unicode:
                                ingred["measurement"] = unicodedata.normalize('NFKD', ingredient["Unit"]).encode('ascii', 'ignore')
                                if ingred["measurement"] is "" or ingred["measurement"] is None:
                                    ingred["measurement"] = "Not specified"
                            else:
                                if ingredient["Unit"] == "" or ingredient["Unit"] is None:
                                    ingred["measurement"] = "Not specified"
                                else:
                                    ingred["measurement"] = ingredient["Unit"]

                            recipe["ingredients"].append(ingred)

                        # Sending recipe to receiving API
                        headers = {'Content-type': 'application/json'}

                        # request = requests.post("http://localhost:8001/recipes/add-recipe/", data=json.dumps(recipe),
                        #                         headers=headers)
                        request = requests.post("http://recipes.mackeydevelopments.com/api/recipes/add-recipe/", data=json.dumps(recipe),
                                                headers=headers)

                        if request.status_code != 201:
                            #########################################
                            # Uh-Oh something went wrong posting the recipe
                            # printing out the recipe without the photo data
                            #########################################
                            print "Recipe POST failed. Status Code: {}".format(request.status_code)
                            recipe.pop('photo')
                            print recipe
                            print request.content
                            time.sleep(50)
                        else:
                            added += 1
                            existing_recipes_names.append(recipe["name"].lower())
                            try:
                                print "Recipe Posted. Name: {}, Time: {}, Status Code: {}".format(recipe["name"],
                                                                             datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
                                                                             request.status_code)
                            # Illegal characters throw an exception
                            except Exception:
                                pass
                            if added == 100:
                                break
                            time.sleep(50)
                    else:
                        print "Skipping that one! " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    print "Skipping that one! " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            else:
                print "Recipe Exists"
        time.sleep(10)
        page += 1
    print "Done with that search term!"
    added = 0
    time.sleep(300)
