N = int(input())
villages = input()

result = ""
index = 0

while index < N:
  if villages[index] == 'H':
    if index + 1 < N and villages[index + 1] == 'H':
      result = ""
      break
    result += 'H'
  else:
    result += 'B'

  index += 1

if result:
  print('YES')
  print(result)
else:
  print('NO')
