try:
    t=int(input("請輸入數量"))
    if 0<=t<=20:
        for i in range(t):
            a=list(map(int,input().split()))
            if len(a)==4:
                if a[1]-a[0]==a[2]-a[1]==a[3]-a[2] :
                    a.append(a[3]+(a[2]-a[1]))
                elif a[1]/a[0]==a[2]/a[1]==a[3]/a[2]:
                    a.append(int(a[3]*(a[2]/a[1])))
                else:
                    print("無法確定序列類型")
                    continue
                print(" ".join(map(str, a)))
except ValueError:
    print("請重新輸入")