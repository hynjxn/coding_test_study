# 백준 1987 알파벳
# https://www.acmicpc.net/problem/1987

import sys
input = sys.stdin.readline
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
R, C = map(int, input().split())

board = list(list(map(lambda x: ord(x)-ord('A'), input().rstrip())) for _ in range(R))

r, c = 0, 0
max_cnt=0
# 알파벳 개수 만큼의 길이를 가진 visited 배열 생성
visited=[False]*26
def dfs(r, c, cnt):
    global max_cnt
    visited[board[r][c]]=True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<R and 0<=nc<C and not visited[board[nr][nc]]:
            dfs(nr, nc, cnt+1)
        max_cnt=max(max_cnt, cnt)
    visited[board[r][c]]=False # 해당 위치를 방문하지 않은 상태로 돌림
dfs(r, c, 1)
print(max_cnt)
