t=int(input("測試數量"))
while t!=0:
    m=input("輸入值")
    x=[]
    for a in str(m):
        x.insert(0,a)
    y=1
    for b in x:
        y*=int(b)
        print(y)
    t-=1