def solution(*args):
    if len(args)==0:
        return -1
    if args[0]>=0:

        a=0
        b=1
        c=0
        for i in range(1,args[0]+1):
            c=a+b
            a=b
            b=c
        return a
    return -1

