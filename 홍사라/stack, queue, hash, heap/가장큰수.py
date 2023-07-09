import sys
sys.stdin=open("input.txt", "r") 

num, m = map(int, input().split())
num = list(map(int, str(num))) 

stack=[] 
for x in num:
    while stack and stack[-1]<x and m>0:
        stack.pop() 
        m-=1 
    stack.append(x) 
if m!=0:
    stack=stack[:-m] 
res=''.join(map(str, stack)) 
print(res)
