# BOJ 11501 주식
# https://www.acmicpc.net/problem/11051

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    profit = 0
    highest = 0
    # 주가 역순으로 접근해야 시간초과 안남 -> 현재의 max값보다 주가가 작으면 차이만큼을 이익에 더한다
    # for문 순서대로 하면 highest를 구할때 리스트 전체 조회해야 하므로 불필요한 연산이 발생함
    for i in range(N-1, -1, -1):
        if arr[i] > highest:
            highest = arr[i]
        else:
            profit += highest - arr[i]
    print(profit)