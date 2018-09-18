f = open("problem.txt")
n = int(f.readline().strip())
integers = list(map(int,f.readline().strip().split()))

products = []

for i in range(n-1):
  products.append(str(integers[i] * integers[i+1]))
  
answer_string = " ".join(products)
print(answer_string)