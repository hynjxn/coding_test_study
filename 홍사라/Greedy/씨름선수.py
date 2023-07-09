import sys
sys.stdin=open("input.txt", "r")
n=int(input())
body=[]
for i in range(n):
    a, b=map(int, input().split())
    body.append((a, b))
# 키로 정렬(내림차순)은 아래와 같은 식으로! 
body.sort(reverse=True)

# 최대값 찾는 과정으로 문제 풀기
# 키가 큰 순으로 정렬되어 있으니, 자기 앞에 더 무거운 사람만 없다면 선발!
largest=0
cnt=0
for x, y in body:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)
