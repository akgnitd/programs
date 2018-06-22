def count_vowels(string):
     count = 0
     a='aeiouAEIOU'
     for letter in string:
         if letter in a:
             count+= 1
             print "vowel ",letter,"at count ",count
     print "number of vowels: ",count

count_vowels(raw_input("Enter String: "))
