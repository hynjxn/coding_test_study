import sys
sys.stdin=open("input.txt", "r")


n = int(input())
seq = list(map(int, input().split()))
tmp = []
lt = 0
rt = n-1 
last = 0
res = ''

while lt<=rt:
    if seq[lt]>last:
				#튜플 형태로 받기
        tmp.append((a[lt], 'L'))
    if seq[rt]>last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp)==0:
        break;
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt=lt+1
        else:
            rt=rt-1
    tmp.clear()

print(len(res))
print(res)
