# Reverses the string using loop

def reverse1(string):
    str=""
    for letter in string:
        str = letter+str
    print "Reverse : ",str,"\n"

reverse1(raw_input("Enter a String: "))
