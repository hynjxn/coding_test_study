# Queue FIFO
import queue

T = int(input())  # 테스트 케이스의 수
for t in range(T):
    # N: 문서의 개수, M: 궁금한 문서가 현재 큐의 몇 번째에 놓여 있는지 (0부터 시작)
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))    # 중요도 리스트

    Q = queue.Queue()
    for i in range(N):
        Q.put((i, importance[i]))

    out = N     # 출력한 문서의 원래 인덱스
    cnt = 0
    while out != M:
        document = Q.get()  # [0,1]
        idx, imp = document
        if imp < max(importance):
            Q.put(document) # 다시 넣기
        else:   # document[1] >= max(importance)
            importance.remove(imp)
            out = idx
            cnt += 1

    print(cnt)
