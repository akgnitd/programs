# Reverse a number

def reversenum(number):
      result = 0
      while number>0:
          remainder = number % 10
          result = result *10 + remainder
          number = number/10
          print number,result
      print "Reverse: ",result

reversenum(int(raw_input("Enter number: ")))
