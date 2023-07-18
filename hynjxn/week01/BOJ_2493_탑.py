# 백준 2493 탑
# https://www.acmicpc.net/problem/2493
# 시간 초과로 https://jjangsungwon.tistory.com/44 참고 후 해결

import sys
input = sys.stdin.readline

N = int(input())
tow_h = list(map(int, input().split()))
result = []

# 시간 초과 코드 -> 맨 오른쪽 탑부터 왼쪽의 탑을 완전 탐색
# while len(tow_h) > 1:
#     i = 1
#     towers = len(tow_h)
#     while True:
#         if i > towers-1:
#             result.append(0)
#             break
#         if tow_h[-1] <= tow_h[-1-i]:
#             result.append(towers-i)
#             break
#         i += 1
#     tow_h.pop()
# print([0]+result[::-1])

# 왼쪽부터 탐색하면서 이전까지의 탑의 정보를 스택에 저장
# 스택에 현재 인덱스의 탑보다 작은 탑이 있다면 pop시킴 -> 오른쪽의 탑이 탐색할 필요가 없기 때문
stk = []

for i in range(N):
    while stk:
        if stk[-1][1] > tow_h[i]:
            result.append(stk[-1][0])
            break
        else:
            stk.pop()
    if not stk:
        # 수신할 수 있는 탑이 없는 경우
        result.append(0)

    stk.append([i+1, tow_h[i]])
print(*result)
