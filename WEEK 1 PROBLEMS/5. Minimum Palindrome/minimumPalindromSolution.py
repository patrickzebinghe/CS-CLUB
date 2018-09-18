f = open('problem.txt')

n = int(f.readline().strip())
s = f.readline().strip()

s_rev = reversed(s)

for i in range(n):
    c1 = s[i:]
    c2 = s[:n-i]
    if c1 == c2:
        print(i)
        break
     