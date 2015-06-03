'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

def prime_factor():
    n = 600851475143
    see_n = []
    i = 2
    see_i = []

    while i * i < n:
        while n % i == 0:
            n /= i
            #see_n.append(n / i)
        i += 1
        see_i.append(i + 1)

    print see_n
    #print see_i
    print n

prime_factor()





