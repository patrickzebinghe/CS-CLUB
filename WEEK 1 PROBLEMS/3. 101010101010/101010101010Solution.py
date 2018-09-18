f=open(“problems.txt”)
n = int(f.readline())
s = f.readline().strip()


last = s[0]
deletions = 0
for l in range(1,len(s)):
  if s[l] == last:
    deletions += 1
  else:
    last = s[l]
print(deletions)