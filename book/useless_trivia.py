# useless trivia program 
# 
#gets personal information from user then
#prints true but useless information
#v1 f.martim

name = raw_input("hi. whats your name? ")

age = raw_input("how old are you? ")
age = int(age)

weight = int(raw_input("Okaay, last question. How many pounds do you weigh? "))

print"\nIf poet see cumming where to email you, he'address you as", name.lower()
print("but if see where mad, he'd call you", name.upper())

called = name * 5
print"\nIf a small child where trying to get your attention "
print("your name would become")
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nyou're over", seconds, "seconds old ")

moon_weight = weight / 6
print("\nDid you know that on the moon you would weigh only", moon_weight, "pounds? ")

sun_weight = weight * 27.1
print("On the sun, you'd weight", sun_weight, "(but not for long...) ")

raw_input ("\n\nPress the enter key to exit. ")

