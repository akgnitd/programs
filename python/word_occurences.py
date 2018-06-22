def word_occurence(string):
     count = dict()
     words = string.split()
     for word in words:
         if word in count:
             count[word]+= 1
         else:
             count[word]= 1
     print "Occurences: ", count

word_occurence(raw_input("Enter String: "))
