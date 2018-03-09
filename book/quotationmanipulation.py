# Quotation Manipulation
# Demonstrates string methods
# francois Martin 19/05/15

# quote from IBM Chairman, Thomas watson, in 1943
quote = "I think there is a world market for maybe five computers"
print "Original quote:"
print quote

print "\nIn uppercase:"
print quote.upper()

print "\nIn lowercase:"
print quote.lower()

print "\nAs a title:"
print quote.title()

print "\nWith a minor replacement:"
print quote.replace("five", "millions of")

print "\noriginal quote is still:"
print quote

raw_input("\n\nPress the enter key to exit.")
