while True:
    try:
        a=list(map(int,input().split()))
        b=len(a)-1
        t=0
        while b!=0:
            t+=a[b]
            b-=1
        c=len(a)-1
        if t/c>59:
            print('no')
        else:
            print('yes')
    except EOFError:
        break
