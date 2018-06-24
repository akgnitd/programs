n,m=map(int,raw_input().split())
a=range(n/2)
a.reverse()
for i in range(n/2):
   pattern= ('.|.'*(2*i+1)).center(m,"-")
   print pattern
print 'WELCOME'.center(m,"-")
for i in a:
   print ('.|.'*(2*i+1)).center(m,"-")
