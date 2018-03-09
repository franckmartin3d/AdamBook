__author__ = 'francoism'
# Losing Battle
# Demonstrates the dreaded infinite loop
# francois martin 27/05/15

print "Your lone hero is surrounded by a massive army of trolls"
print "Their decaying green bodies stretch out, melting into the horizon."
print "Your hero unleash his sword and begins the last fight of his life"

health = 10
trolls = 0
damage = 3

while health != 0:
    trolls += 1
    health = health - damage

    print "your hero swing and defeats an evil troll," \
            "but takes", damage, "damage points. \n"

print "your hero fought valiantly and defeated", trolls, "trolls."
print "But alas your hero is no more!"

raw_input("\n\nPress exit to quit.")