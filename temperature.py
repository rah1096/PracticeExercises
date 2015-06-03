from __future__ import print_function


def c_to_f(C):
    #takes celsius temp and convert to fahrenheit
    return float(C * 9/5 +32)

def f_to_c(F):
    #takes fahrenheit temp and convert to celsius
    return float((F - 32) * 5/9)

temp1 = 72

print("{} degrees F = {} degrees C" .format(temp1, f_to_c(temp1)))

temp2 = 37

print("{} degrees C = {} degrees F" .format(temp2, c_to_f(temp2)))

x = float((72 - 32) * 5/9)

print(float(x))