__author__ = 'francoism'
# Finicky Counter
# Demonstrate the break and continue statement
# Francois Martin 28/05/15

count =  0
while True:
    count += 1
    # end loop if count is greater than 10
    if count > 10:
        break
    # skip 5
    if count == 5:
        continue
    print count

raw_input("\n\press enter key to exit")
