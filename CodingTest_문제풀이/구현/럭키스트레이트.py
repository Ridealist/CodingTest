"""
a = b

<=>

a - b = 0
"""


num = input()

n = len(num)
half = n//2

l = 0
# summary = 0
for i in range(0, half):
    l += int(num[i])
    # summary += int(num[i])

r = 0
for j in range(half, n):
    r += int(num[j])
    # summary -= int(num[j])

# print(l, r)

# if summary == 0:
if l == r:
    print("LUCKY")
else:
    print("READY")