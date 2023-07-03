import sys
input = sys.stdin.readline

N = int(input())
tow_h = list(map(int, input().split()))
result = [0] # 어차피 맨 왼쪽 탑의 신호는 수신 불가능
while len(tow_h) > 1:
    i = 1
    while True:
        if i > N-1 :
            result.append(0)
            break
        if tow_h[-1] <= tow_h[-1-i]:
            result.append(N-i)
            break
        i += 1

