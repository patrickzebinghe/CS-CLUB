f = open(”problem.txt”)
n = int(f.readline())
t = int(f.readline())
preptimes = list(map(int,f.readline().strip().split()))

preptimes.sort()

served = 0
for p in preptimes:
  t -= p
  if t<0:
    break
  served += 1
  
print(served)