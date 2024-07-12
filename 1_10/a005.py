try:
    t=int(input("請輸入數量"))
    a=[]
    if 0<=t<=20:
        for i in range(0,t):
            a=list(map(int,input().split()))
            if len(a)==4:
                if a[1]-a[0]==a[2]-a[1]==a[3]-a[2] :
                    a.append(int(a[3]+(a[2]-a[1])))
                    print(" ".join(map(str, a)))
                elif a[1]/a[0]==a[2]/a[1]==a[3]/a[2]:
                    a.append(int(a[3]*(a[2]/a[1])))
                    print(" ".join(map(str, a)))
            if i == t : break
except ValueError:
    print("請重新輸入")