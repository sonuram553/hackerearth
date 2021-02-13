T = int(input())
result = []

for i in range(T):
  x, y, a, b = [int(n) for n in input().split()]

  if x * y == a + b:
    result.append("Yes")
  else:
    result.append("No")

for value in result:
  print(value)

""" 
Take for example the sequence
00011
here we can see 6 '01' sub sequences
and 0 '10' sub sequences
now if we exchange a 0 with the adjacent 1 see what happens
it becomes
00101
in exchanging 01 for 10 we have destroyed a '01' sub sequence and created a '10' sub sequence
similarly on exchanging 10 for 01 we destroy a '10' and create a '01'
Thus the total number of '10' and '01' sub sequences in a sequence of fixed number of 0s and 1s is constant
Now if we take
00000...(x times)11111...(y times)
the number of '01' sub sequences is x*y
the number of '10' sub sequences is 0
total '01' or '10' sub sequences are x*y
so a+b=x*y
So we just have to check the condition

if( x*y==a+b): print "Yes"
else: print "No" 
"""
