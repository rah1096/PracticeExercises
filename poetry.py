import random

nouns = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extrovert', 'gorilla']
verbs = ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes', 'curdles']
adjectives = ['furry', 'balding', 'incredulous', 'fragrant', 'exuberant', 'glistening']
prepositions = ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within']
adverbs = ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously']



def poetry():
    structure = []
    count = 0

    random.shuffle(nouns)
    random.shuffle(adjectives)
    random.shuffle(prepositions)
    random.shuffle(adverbs)

    # verb = random.choice(verbs)
    # adjective = random.choice(adjectives)
    # preposition = random.choice(prepositions)
    # adverb = random.choice(adverbs)

    for i in nouns:
        structure.append(i)
        nouns.remove(i)
        count += 1
        if count == 3:
            break
    for i in verbs:
        structure.append(i)
        verbs.remove(i)
        count += 1
        if count == 6:
            break
    for i in adjectives:
        structure.append(i)
        adjectives.remove(i)
        count += 1
        if count == 9:
            break
    for i in prepositions:
        structure.append(i)
        prepositions.remove(i)
        count += 1
        if count == 11:
            break
    for i in adverbs:
        structure.append(i)
        adverbs.remove(i)
        count += 1
        if count == 12:
            break

    first_adj_letter = []

    second_adj_letter = []

    for n in structure[6]:
        first_adj_letter.append(n[0])

    for n in structure[8]:
        second_adj_letter.append(n[0])


    if first_adj_letter[0] in ['a', 'e', 'i', 'o', 'u']:
        print "An {} {}" .format(structure[6], structure[0])
        print ""
        print "An {} {} {} {} the {} {}" .format(structure[6], structure[0], structure[3], structure[9], structure[7],\
                                                 structure[1])
        print "{}, the {} {}" .format(structure[11], structure[0], structure[4])
    else:
        print "A {} {}" .format(structure[6], structure[0])
        print ""
        print "A {} {} {} {} the {} {}" .format(structure[6], structure[0], structure[3], structure[9], structure[7],\
                                                 structure[1])
        print "{}, the {} {}" .format(structure[11], structure[0], structure[4])


    if second_adj_letter[0] in ['a', 'e', 'i', 'o', 'u']:
        print "the {} {} {} an {} {}" .format(structure[1], structure[5], structure[10], structure[8], structure[2])
    else:
        print "the {} {} {} a {} {}" .format(structure[1], structure[5], structure[10], structure[8], structure[2])


poetry()


