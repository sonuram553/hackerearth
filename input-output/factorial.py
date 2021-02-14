N = int(input())

fact = 1
index = 2

while index <= N:
  fact *= index
  index += 1

print(fact)