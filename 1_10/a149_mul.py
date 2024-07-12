t=int(input("測試數量"))
while t!=0:
    m=input("輸入值")
    x=[int(a) for a in m]
    
    y=1
    for b in x:
        y*=b
    print(y)
    t-=1