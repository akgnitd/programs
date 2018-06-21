def prime(number):
      count=0
      for num in range(2,number):
          if number%num == 0:
              count+=1
              break
      if count == 0:
          print "prime"
      else:
          print "not prime"
