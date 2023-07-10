# Stack LIFO
N = int(input())  # 5
towers = list(map(int, input().split()))  # 6 9 5 7 4

stack = []

ans = []

for i in range(N):  # 0 1 2 3 4
    # 현재 송신 타워
    # (idx, 높이)

    # stack에 원소가 있다면 루프 문을 돌기
    while stack:
        # 현재 타워의 높이 보다 작은 왼쪽 타워 -> 앞으로 쓸모 없음
        if stack[-1][1] < towers[i]:
            stack.pop()
        else:   # stack[-1][1] > towers[i]
            ans.append(stack[-1][0]+1)
            break

    # 이번 송신 타워가 아직 수신 타워를 찾지 못 함
    if len(stack) == 0:
        ans.append(0)

    # 이번 타워(i, 높이)를 스택에 추가
    stack.append((i, towers[i]))

print(*ans, sep=' ')

# 매 타워마다 왼쪽에 위치한 타워에 대해서 for문을 돌리며 가능한 경우 찾기 (-> 시간 초과)

# answer += str(stack[-1][0]+1) 형태로 출력하는 것 보다 (-> 시간 초과)
# 배열을 print(*ans, sep=' ')로 출력하는 것이 더 빠름 (시간 초과 해결)