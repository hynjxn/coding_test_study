import sys
sys.stdin=open("input.txt", "r") 

# 창고 높이 조정 : 가장 높은 곳 상자 1개를 -> 가장 낮은 곳으로 

row = int(input())
columns = list(map(int, input().split()))
m = int(input())

for _ in range(m):    
    columns[0]=columns[0]-1
    columns[-1]=columns[-1]+1
    columns.sort(reverse=True)

print(columns[0]-columns[-1])
