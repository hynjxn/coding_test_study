# Stack LIFO

def push(stack1, stack2, num1, ans):
    if (num1 not in stack1) or (len(stack1) == 0):
        return stack2
    else:
        num2 = 0

        while num2 != num1:
            num2 = stack1.pop()
            stack2.append(num2)
            ans.append("+")
        return stack2

# main
n = int(input())  # 8
input_list = []  # 4 3 6 8 7 5 2 1
for i in range(n):
    input_list.append(int(input()))

stack1 = [i for i in range(1, n + 1)]
stack1.reverse()    # [8, 7, 6, 5, 4, 3, 2, 1]
stack2 = []
ans = []  # +, -, NO

for num in input_list:
    # stack2가 비어 있음
    if len(stack2) == 0:
        stack2 = push(stack1, stack2, num, ans)
        stack2.pop()
        ans.append("-")
    # stack2가 비어 있지는 않지만, push 해야 함
    elif stack2[-1] < num:
        push(stack1, stack2, num, ans)
        stack2.pop()
        ans.append("-")
    elif stack2[-1] == num:
        stack2.pop()
        ans.append("-")
    else:  # stack2[-1] > num
        ans = ["NO"]
        break

for a in range(len(ans)):
    print(ans[a])