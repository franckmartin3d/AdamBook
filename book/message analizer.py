__author__ = 'francoism'
# Message Analyzer
# Demonstrates the len() function and the in operator
# Francois Martin 27/7/15

message = raw_input("Enter a message: ")

print "\nthe lenght of your message is:", len(message)

print "\nThe most common letter in the english language 'e',",
if "e" in message:
    print "is in your message."
else:
    print "is not in your message."

raw_input("\n\npress the enter key to exit")