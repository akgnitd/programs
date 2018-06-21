# Reverses the string

def reverse1(string):
    print "Reverse : ",string[::-1],"\n"

reverse1(raw_input("Enter a String: "))

# Reverses each word in a string without changing its index.

def reverse2(string):
    print "Reverse with unchanged index of each word: ",' '.join(string.split()[::-1])[::-1],"\n"

reverse2(raw_input(("Enter another String: ")))
