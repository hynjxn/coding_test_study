import sys
sys.stdin=open("input.txt", "r") 

lst = input()
lst = list(map(str, str(lst)))

stack = []

for x in lst:  
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=='*':
            res1=stack.pop()
            res2=stack.pop()
            stack.append(res2*res1)
        elif x=='/':
            res1=stack.pop()
            res2=stack.pop()
            stack.append(res2/res1)
        elif x=='+':
            res1=stack.pop()
            res2=stack.pop()
            stack.append(res2+res1)
        elif x=='-':
            res1=stack.pop()
            res2=stack.pop()
            stack.append(res2-res1)

print(stack[0])
