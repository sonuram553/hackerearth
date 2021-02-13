dic = {
  'G': 'C',
  'C': 'G',
  'T': 'A',
  'A': 'U'
}
str = input()
res = ''

for c in str:
	if c.upper() in dic.keys():
		res += dic[c.upper()]
	else:
		res = "Invalid Input"
		break

print(res)
