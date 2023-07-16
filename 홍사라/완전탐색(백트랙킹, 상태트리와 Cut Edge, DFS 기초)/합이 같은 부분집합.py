import sys
sys.stdin=open("input.txt", "r")
def DFS(L, sum):  
    if sum>total//2: 
        return 
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0) 
    else:
        DFS(L+1, sum+a[L]) #왼쪽 노드('부분집합의 원소로 사용한다' 노드)
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0, 0)
    print("NO")
