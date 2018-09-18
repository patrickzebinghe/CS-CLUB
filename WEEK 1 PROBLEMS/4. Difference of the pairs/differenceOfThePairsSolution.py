f = open('problem.txt')
n = int(f.readline())
t = int(f.readline())
arr = list(map(int,f.readline().strip().split()))

works = 0
arr.sort()
while len(arr) > 0:
f = arr.pop(0)
t = k + f

for i,c in enumerate(arr):
    if c == t:
        works += 1
        break
    if c > t :
        break

print(works)