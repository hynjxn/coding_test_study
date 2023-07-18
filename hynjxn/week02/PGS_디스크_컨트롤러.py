'''
작업 소요 시간 짧은 순 + 현 시점에 요청 왔는지

요청
[작업 요청 시점, 작업 소요 시간]
'''

'''
문제 풀이 방향은 생각했으나
별도의 sort 없이 현 시점에 수행 가능한 작업만 heap에 넣어서 처리하는 로직을 생각하지 못해서
풀이 찾아보았음
https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99

'''
import heapq


def solution(jobs):
    # start: 이전 작업 시작 시간, end: 이전 작업 종료 시간
    start, end, tot_time = -1, 0, 0
    i = 0  # 모든 작업 처리했는지 확인하는 변수
    N = len(jobs)
    heap = []

    while i < len(jobs):
        # 현재 수행할 수 있는 작업 heap에 넣기
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:
            # jobs와 순서 반대임 -> [작업 소요 시간, 작업 요청 시점]
            now_job = heapq.heappop(heap)
            start = end
            end += now_job[0]
            tot_time += end - now_job[1]
            i += 1
        else:
            end += 1
    return tot_time // N
