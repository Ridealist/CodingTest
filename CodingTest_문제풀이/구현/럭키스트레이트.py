num = input()

n = len(num)
half = n//2

l = 0
for i in range(0, half):
    l += int(num[i])

r = 0
for j in range(half, n):
    r += int(num[j])

# print(l, r)

if l == r:
    print("LUCKY")
else:
    print("READY")