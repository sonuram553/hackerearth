T = int(input())
result = []

for t in range(T):
  str_a = input()
  str_b = input()

  char_map_a = {}
  char_map_b = {}

  for ch in str_a:
    if ch in char_map_a.keys():
      char_map_a[ch] += 1
    else:
      char_map_a[ch] = 1

  for ch in str_b:
    if ch in char_map_b.keys():
      char_map_b[ch] += 1
    else:
      char_map_b[ch] = 1

  diff = 0

  for ch in char_map_a:
    if ch in char_map_b.keys():
      if char_map_a[ch] != char_map_b[ch]:
        diff += abs(char_map_a[ch] - char_map_b[ch])
    else:
      diff += char_map_a[ch]

  for ch in char_map_b:
    if not(ch in char_map_a.keys()):
      diff += char_map_b[ch]

  result.append(diff)

for value in result:
  print(value)
