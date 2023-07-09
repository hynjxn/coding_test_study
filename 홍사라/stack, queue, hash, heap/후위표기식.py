import sys
sys.stdin=open("input.txt", "r") 

lst = input()

stack = []
res = ''

for x in lst:  
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            # stack이 비어있지 않고
            # 지금 들어가는 * or / 보다 왼쪽에 있었던(우선순위가 높은) * or /이기에
            # 계속 빼내기
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                # stack에서 pop + res에 추가
                res+=stack.pop()
            # 다 빼냈으면 x(자기자신)를 stack에 추가
            stack.append(x)
        elif x=='+' or x=='-':
            # + or -는 최하위우선순위니까 일단 다 빼되 
            # '(' 만나기 전에. 즉 괄호 안에 있는 거 다 빼기
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':  
                res+=stack.pop()
            # 여는 괄호를 없애버리기
            stack.pop()

# stack에 연산자가 남아있다면
while stack: 
    res+=stack.pop()
print(res)
