import sys
sys.stdin=open("input.txt", "r")

from collections import deque
n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
weights = deque(weights)
cnt = 0

# 구명보트의 최소 개수를 구하려면
# 무게 순으로 오름차순 정렬을 시킨 후에
# [50, 60, 70, 90, 100]

while weights:
    if len(weights)==1:
        cnt+=1 
        break
    if weights[0]+weights[-1] <= m:
        cnt+=1
        weights.popleft()
        weights.pop()
    else: 
        cnt+=1
        weights.pop()

print(cnt)
