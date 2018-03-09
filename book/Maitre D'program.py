__author__ = 'francoism'
# Maitre D'
# Demonstrate treating value as condition
# francois martin 27/05/15

print "welcome to the Chateau D' food"
print "It seems we are quite full this evening.\n"

money = int(raw_input("How many dollars do you slip the Maitre d'?"))

if money:
    print "Ah, i am reminded of a table. right this way."
else:
    print "Please,sit it may be a while"

raw_input("\n\npress the enter key to exit.")
