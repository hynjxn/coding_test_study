# BOJ 4358 생태학 (파이썬 defaultdict로 해결)
# https://www.acmicpc.net/problem/4358

import sys
from collections import defaultdict

input = sys.stdin.readline
dd = defaultdict(int)
tot = 0

while True:
    name=input().rstrip()
    if name =="":
        break
    dd[name] += 1
    tot += 1

for name, cnt in sorted(dd.items()):
    # print(name, round(cnt/tot*100,4)) -> 이걸로 하면 오답 나옴
    print(name, f"{(cnt/tot)*100:.4f}")


'''
float에 대한 round는 예상과 다를 수 있다고 함
round(0.5) 와 round(-0.5) 는 모두 0 이고, round(1.5) 는 2
round(2.675, 2) 는 2.68 대신에 2.67 을 제공

결론: round 쓰지 말자 ^_^
'''
