import sys
sys.stdin=open("input.txt", "r") 

a = input()
b = input()
sH = dict() 

for x in a:
    sH[x]=sH.get(x, 0)+1
for y in b:
    sH[y]=sH.get(y, 0)-1 

for z in a: 
    if(sH.get(z)>0):
        print("NO")
        break 
else:
    print("YES")
