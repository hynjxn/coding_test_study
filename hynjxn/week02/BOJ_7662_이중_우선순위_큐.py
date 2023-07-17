# BOJ 7662 이중 우선순위 큐
# https://www.acmicpc.net/problem/7662
'''
최대 힙, 최소 힙 두 개를 사용하는 것은 구현하였으나
두 힙의 상태를 맞춰주기 위해 최대 힙에서 heappop한 것을 최소 힙에서 remove()함 -> 너무나 시간초과

visited 배열을 만들고, 힙에 id를 부여하여 해당 값이 삭제된 값인지를 확인 하는 방법을 풀이 참고하였음
https://esoongan.tistory.com/71
'''

import sys
import heapq

def sync(heap):
    while heap and visited[heap[0][1]] == 0:
        heapq.heappop(heap)

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_heap, max_heap = [], []
    k = int(input())
    visited = [False] * k
    for i in range(k):
        letter, n = input().split()
        n = int(n)
        if letter == "I":
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            visited[i] = True
        if letter == "D":
            if n == 1:
                sync(min_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    d = heapq.heappop(max_heap)
            elif n == -1:
                sync(max_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    d = heapq.heappop(min_heap)
        sync(min_heap)
        sync(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')