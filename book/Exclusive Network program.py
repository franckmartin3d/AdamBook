__author__ = 'francoism'
# Exclusive Network
# Demonstrate logicals operation conditioms
# Francois Martin

security = 0
username =""
while not username:
    username = raw_input("username: ")

psssword = ""
while not password:
    password = raw_input("password: ")

if username == "m.daswon" and password == "secret":
    print "Hi, mike."
    security = 5

elif username == "s.meier" and password == "civilisation":
    print "Hey, sid."

elif username == "s.miyamoto" and password == "mariobros":
    print "Whats up shigeru"

elif username == "w.wright" and password == "thesims":
    print "what up will"

elif username == "guest" and password =="guest":
    print "welcome guest"
    security = 1

else :
    print "GTFO wrong password"

raw_input("\n\npress enter to quit")


