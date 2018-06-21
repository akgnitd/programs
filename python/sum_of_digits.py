def sum_of_digits(number):
     digit_sum=0
     while number>0:
         remainder=number%10
         digit_sum=remainder+digit_sum
         number=number/10
     print "Sum is: ",digit_sum


sum_of_digits(int(raw_input("Enter number: ")))
