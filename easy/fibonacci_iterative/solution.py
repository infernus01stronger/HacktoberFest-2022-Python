def answer(n):
    a=0
    b=1
    c=0
    for i in range(1,n+1):
        c=a+b
        a=b
        b=c
    print(a)
n=int(input())
answer(n)

