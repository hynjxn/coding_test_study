# 프로그래머스 2022 KAKAO BLIND RECRUITMENT : k진수에서 소수 개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335#

import math

def is_prime_number(x):
    # 개선된 소수 판별 알고리즘
    # 2부터 x의 제곱근까지 나누어 떨어지는 수가 있는지 확인
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def n_to_k_binary(n, k):
    # 10진수를 k진수로 변환하는 알고리즘
    result = []
    while True:
        a, b = divmod(n, k)  # divmod() : 몫, 나머지를 한번에 tuple로 반환
        result.append(b)
        n = a
        if n < k:
            result.append(n)
            break
    return ''.join(map(str, result[::-1]))


def solution(n, k):
    k_jin_su = n_to_k_binary(n, k) # n을 k진수로 변환
    prime_cand = k_jin_su.split('0') # 0을 기준으로 숫자를 구분함
    cnt = 0
    for x in prime_cand: # 구분한 숫자가 소수인지 판별
        if x != '':
            if is_prime_number(int(x)):
                cnt += 1
    return cnt



