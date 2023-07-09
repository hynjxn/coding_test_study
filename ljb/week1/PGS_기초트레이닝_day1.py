# 문자열 출력하기 (https://school.programmers.co.kr/learn/courses/30/lessons/181952)
str = input()
print(str)

# a와 b 출력하기 (https://school.programmers.co.kr/learn/courses/30/lessons/181951)
a, b = map(int, input().strip().split(' '))
print(f"a = {a}",f"b = {b}",sep = "\n")

# 문자열 반복해서 출력하기 (https://school.programmers.co.kr/learn/courses/30/lessons/181950)
a, b = input().strip().split(' ')
b = int(b)
print(a*b)

# 대소문자 바꿔서 출력하기 ()
str = list(input())
new_str = []
j = 0
for i in str:
    if i.isupper():
        new_str.append(i.lower())
    else:
        new_str.append(i.upper())
while j < len(new_str):
    print(new_str[j],end="")
    j += 1
'''
--- 예시 답안 ---
print(input().swapcase())
'''
# 특수문자 출력하기 (https://school.programmers.co.kr/learn/courses/30/lessons/181948)
print("!@#$%^&*(\\\'\"<>?:;")
'''
--- 예시 답안 ---
print(r'!@#$%^&*(\'"<>?:;')
'''