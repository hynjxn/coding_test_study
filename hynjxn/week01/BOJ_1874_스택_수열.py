# 백준 1874 스택 수열
# https://www.acmicpc.net/problem/1874

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque() # 스택을 통해 만들 수열
for _ in range(n):
    arr.append(int(input()))

now = 1
stk = [] # 수열을 만들 스택
result = []

while arr:
    if stk and stk[-1] == arr[0]:
        # 스택에서 pop하는 경우
        # 수열의 현재 값이 스택의 top과 같으면 pop한다
        stk.pop()
        arr.popleft()
        result.append("-")
        continue
    if now > arr[0]:
        # 오름차순으로 push해서는 주어진 수열을 만들 수 없는 경우
        print("NO")
        exit()
    elif now <= arr[0]:
        # 스택에 push하는 경우
        stk.append(now)
        result.append("+")
        now += 1 # 오름차순을 지키기 위해

for p in result:
    print(p)