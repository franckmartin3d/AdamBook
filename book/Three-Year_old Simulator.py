__author__ = 'francoism'
# Three-year-old simulator
# Demonstrate the while loop
# Franck Martin 27/05/15

print "welcome to the 'Three-Year old simulator'\n"
print "This program simulates a conversation with a three-year-old child."
print "Try to stop the madness.\n"

response = ""

while response != "because":
    response = raw_input("Why\n")

    print "Oh. Okay. "

raw_input("\n\nPress enter to exit.")