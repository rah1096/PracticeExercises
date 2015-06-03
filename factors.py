pos_num = int(raw_input("Enter a positive integer: "))

for n in range(1, pos_num + 1):
    if pos_num % n == 0:
        print('{} is a divisor of {}' .format(n, pos_num))





