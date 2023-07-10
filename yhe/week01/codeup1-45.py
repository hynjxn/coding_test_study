# ('"C:\Download\\\'hello\'.py"')

# print('"Hello\\nWorld"')

'''
a = "fighting"       # 9번
print(a)'''

'''a = input()        # 10번
a = int(a)
print(a)'''

'''f = input()        #11번
f = float(f)
print(f)'''

'''a = input()      # 12번
b = input()
a  = int(a)
b = int(b)
print(a)
print(b)'''

'''a = input()           # 13번
b = input()
print(b)
print(a)'''

'''f = input()           # 14번
f = float(f)
print(f)
print(f)
print(f)'''

'''a,b = input().split()       # 15번
a = int(a)
b = int(b)
print(a)
print(b)'''

'''a = input()      # 16번
b = input()
print(b,a)'''

'''s = input()     # 17번
print(s,s,s)'''

'''
a,b = input().split('')    # 18번
print(a,b,sep=':')
'''

'''
y,m,d = input().split('.')      # 19번
print(d,m,y,sep='-')
'''

'''a,b = input().split('-')       #20번
print(a,b,sep='')'''

'''a = input()              # 21번
print(a[0])
print(a[1])'''

'''a = input()                    # 22번
print(a[0:2],a[2:4],a[4:7])'''

'''a = input().split(':')      # 23번
print(a[1])'''

'''a,b = input().split()        #24
s = a + b
print(s)'''

'''a,b = input().split()      # 25
c = int(a)+int(b)
print(c)'''

'''a = float(input())        #26
b = float(input())
print(a + b)'''

'''a = input()               #27
n = int(a)
print('%x'%n)'''

'''a = input()              #28
n = int(a)
print('%X'%n)'''

'''a = input()         #29
n = int(a,16)
print('%o'%n)'''

'''n = ord(input())     #30
print(n)'''

'''c = int(input())     #31
print(chr(c))'''

'''n = int(input())     #32
print(-n)'''

'''a = ord(input())      #33
print(chr(a+1))'''

'''a,b = input().split()     #34
a = int(a)
b = int(b)
s = a- b
print(s)'''

'''a, b = map(float, input().split())     #35
m = a * b
print(m)'''

'''w,n = input().split()   # 36
print(w*int(n))'''

'''n = input()          # 37
s = input()
print(int(n)*s)'''

'''
a = int(input())     #38
b = int(input())
c = a**b
print(c)'''

'''a,b = map(float,input().split())    #39
c = a**b
print(c)'''

'''a,b = map(int,input().split())      #40 
print(a//b)'''

'''a,b = map(int,input().split())      # 41
print(a%b)'''

'''a = float(input())                #42
print(format(a,".2f"))'''

'''a,b = map(float, input().split())  #43
print(format(a//b,".4f"))'''

'''a,b = map(int, input().split())           #44
print(a+b,a-b,a*b,a//b,a%b,format(a/b,".2f"),sep='\n')'''

'''a,b,c = map(int,input().split())             #45
print(a+b+c,format((a+b+c)/3,".2f"),sep=" ")'''

'''a = int(input())         #46
print(a<<1)'''

'''a,b = map(int,input().split())      # 47
print(a<<b)'''

'''a,b = map(int,input().split())   # 48
print(a<b)'''

'''a,b = map(int,input().split())   # 49
print(a<=b)'''

'''a,b = map(int,input().split())   # 50
print(a>=b)'''

'''a,b = map(int,input().split())   # 51
print(a!=b)'''

'''n = int(input())            # 52
print(bool(n))'''

'''n = int(input())            # 53
print(not n)'''

'''a,b = input().split()         # 54
print(bool(int(a))and bool(int(b)))'''

'''a,b = input().split()         # 55
print(bool(int(a)) or bool(int(b)))'''

'''a,b = input().split()                         # 56
c = bool(int(a))      # 0 false, 그 외 true
d = bool(int(b))
print((c and (not d)) or ((not c) and d))'''

'''a,b = input().split()         # 57
a = bool(int(a))
b = bool(int(b))
print(a==b)'''

'''a, b = input().split()     # 58
c= bool(int(a))
d= bool(int(b))
# print(not (c or d))
if(c == False and d == False):
    print("True")
else:
    print("False")'''

'''a = int(input())     # 59 비트단위로 NOT
print(~a)'''

'''a,b = map(int,input().split())       # 60
print((a & b))'''

'''a,b = map(int,input().split())       # 61
print((a | b))'''

'''a,b = map(int,input().split())       # 62
print((a ^ b))'''