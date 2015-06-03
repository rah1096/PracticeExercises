'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''

def three_and_five():
    result_3 = []
    result_5 = []
    result_3_and_5 = []

    for i in range(1, 1000):
        if i % 3 == 0 and i % 5 == 0:
            result_3_and_5.append(i)
        if i % 3 == 0:
            result_3.append(i)
            if i % 5 == 0:
                result_3.remove(i)
        if i % 5 == 0:
            result_5.append(i)
            if i % 3 == 0:
                result_5.remove(i)

    print sum(result_3 + result_5 + result_3_and_5)



three_and_five()