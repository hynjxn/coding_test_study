# 백준 1966 프린터 큐
# https://www.acmicpc.net/problem/1966

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    q = deque([[i, p] for i, p in enumerate(priority)]) # 현재 문서의 순서와 중요도를 큐에 저장
    # 이후 priority는 남아있는 문서의 최대 중요도를 확인하기 위해 사용
    priority.sort()
    cnt = 0
    while q:
        if q[0][1] == priority[-1]:
            cnt += 1
            i, p = q.popleft()
            priority.pop()
            if i == M:
                print(cnt)
                break
        else:
            q.append(q.popleft())
