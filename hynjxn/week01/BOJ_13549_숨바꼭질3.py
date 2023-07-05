# 백준 13549 숨바꼭질
# https://www.acmicpc.net/problem/13549

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
if N>=K:
# K가 N보다 뒤에 있을 경우에는 -1로만 이동
    print(N-K)
    exit()

visited = [-1] * 100001
visited[N]=0
q=deque([N])
while q:
    X=q.popleft()
    now = visited[X]
    if X==K:
        break
    for next in [X*2, X-1, X+1]:
        if next < 0 or next > 100000 or visited[next]!=-1:
            continue
        if next==X*2:
            # X=0일때 무한루프 방지
            if X == 0:
                continue
            visited[next]=now
            # X*2 순간이동이 다른 연산보다 먼저 실행되도록 맨 앞에 push
            q.appendleft(next)
        else:
            visited[next]=now+1
            q.append(next)
print(visited[K])