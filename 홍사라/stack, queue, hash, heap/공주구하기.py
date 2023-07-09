import sys
from collections import deque
sys.stdin=open("input.txt", "r") 

n, k = map(int, input().split())

a = []
for i in range(1, n+1):
    a.append(i)
a = deque(a)

while len(a)!=1:
    for _ in range(k-1):
        cur=a.popleft()
        a.append(cur) 
    a.popleft()
   

print(a[0])   
