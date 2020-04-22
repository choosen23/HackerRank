# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
N = int(input())
d = []
for i in range(0,N):
    d.append(input())

res = list(Counter(d).values())

print(len(res))
for i in res: 
    print(i, end =" ")  








