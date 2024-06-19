while True :
    n=int(input())
    if 0<n<=50000:
        break
    # else :
    #     print("輸入的數字必須大於0，請重新輸入。")

count_0 = 0
count_1 = 0
count_2 = 0
for a in range(1,n+1) :
    b = int(input())
    if b % 3==0:
        count_0+=1
    elif b % 3==1:
        count_1+=1
    else :
        count_2+=1
    a+=1
    # print(a)
print(count_0,count_1,count_2)