__author__ = 'francoism'
# Craps Roller
# demonstrates random number generation
# Francois martin 25*05/2015

import random

# generate random numbers 1- ^
die1 = random.randrange(6) + 1
die2 = random.randrange(6) + 1

total = die1 + die2

print "you rolled a", die1, "and a", die2, "for a total of", total

raw_input("\n\nPress the enter key to exit.")

