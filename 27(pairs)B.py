f = open('')
n = int(f.readline())
s = [0]
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    s = [a + b for a in s for b in pair]
    s = {x % 3: x for x in sorted(s)}.values()
print(max(x for x in s if x % 3 == 0))
