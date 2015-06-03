from random import random

total_A_wins = 0
total_B_wins = 0

trials = 100000
for trial in range(0, trials):
    A_win = 0
    B_win = 0
    if random() < .87:
        A_win += 1
    else:
        B_win += 1
    if random() < .65:
        A_win += 1
    else:
        B_win += 1
    if random() < .17:
        A_win += 1
    else:
        B_win += 1
    if A_win > B_win:
        total_A_wins += 1
    else:
        total_B_wins += 1
    print A_win
    print B_win

print "Probability A wins:", total_A_wins #/ float(trials)
print "Probability B wins:", total_B_wins #/ float(trials)

print random()


