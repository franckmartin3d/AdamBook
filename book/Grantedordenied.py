__author__ = 'francoism'

# Granted or denied
# demonstrate the if - else structure
# francois martin 26/05/15

print "Welcome to Sysstem security Inc."
print "- where security is our middel name\n"

password = raw_input("Enter your password: ")

if password == "secret":
    print "access granted"
else:
    print "access Denied"

raw_input("\n\npress enter to exit.")