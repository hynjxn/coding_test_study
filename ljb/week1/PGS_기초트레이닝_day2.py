# 덧셈식 출력하기 (https://school.programmers.co.kr/learn/courses/30/lessons/181947)
a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a+b}')

# 문자열 붙여서 출력하기 (https://school.programmers.co.kr/learn/courses/30/lessons/181946)
str1, str2 = input().strip().split(' ')
print(str1+str2)
'''
---예시 답안---
print(input().strip().replace(' ', ''))
print(''.join(input().strip().split(' ')))
'''
# 문자열 돌리기 (https://school.programmers.co.kr/learn/courses/30/lessons/181945)
str = input()
for i in str:
    print(i)

# 홀짝 구분하기 (https://school.programmers.co.kr/learn/courses/30/lessons/181944)
a = int(input())
if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')
'''
---예시 답안---
N = int(input())
print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")
'''
# 문자열 겹쳐쓰기 (https://school.programmers.co.kr/learn/courses/30/lessons/181943)
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer