import sys
sys.stdin=open("input.txt", "r")
n=int(input())
meeting=[]
for i in range(n):
    s, e=map(int, input().split())
    meeting.append((s, e)) #list에 tuple형태로 append. i.e., [(1,2), (3,4) ...] 

# 이 문제는 회의가 끝나는 시간을 기준으로 정렬해야한다. 
# 회의실에서 '최대한 많은 회의'를 해야하니까, 빨리 '끝나는 시간'이 중요! 

#정렬하는 key의 기준=> lambda x: (x[1],x[0])
# x[1]은 e, x[0]은 s니까 -> 'e'('x[1]')을 기준으로 정렬하겠다. 
meeting.sort(key=lambda x : (x[1], x[0])) 

et=0 #end time (회의 끝나는 시각)
cnt=0
for s, e in meeting:
    if s>=et: # 크거나 같아야지! 
        et=e
        cnt+=1
print(cnt)
