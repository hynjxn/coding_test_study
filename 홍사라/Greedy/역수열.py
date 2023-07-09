import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split())) #역수열
seq=[0]*n

# 1~n까지 오름차순 정렬된 배열(원수열)이 있다고 가정하고
# seq이라는 리스트에 집어넣는 방식


for i in range(n):
    for j in range(n):
        # 빈공간을 찾고 자기 자리 찾아가는 것
        #i라는 숫자(i+1)의 앞에 몇개의 숫자가 있어야 하는지
        #j자리가 0인지. 즉 이미 들어간 다른 숫자가 없는지
        if(a[i]==0 and seq[j]==0): 
            seq[j]=i+1 
            break #j를 break. 자기(i+1) 자리 잘 찾아서 들어갔으니까 
        elif seq[j]==0: #빈자리인 것. 아직 자기 자리 못 찾은 것! 
            a[i]-=1 #계속 자리 앞으로. -> 그리고 0이 됐을 때 위에 if문으로 간다면!

for x in seq:
    print(x, end=' ')
