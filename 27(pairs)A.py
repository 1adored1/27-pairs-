f = open('')
n = int(f.readline())
s = [0]

mx = -float('inf')
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    s = [a + b for a in s for b in pair]
for x in s:
    if x % 3 == 0:
        mx = max(mx, x)
print(mx)

