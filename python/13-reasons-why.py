A, B, C = [int(n) for n in input().split()]

temp = A
A = B
B = temp

A *= C
B += C

print(A, B)
