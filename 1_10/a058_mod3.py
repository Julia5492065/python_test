while True :
    try :
        n=int(input())
        if n > 0 and n<=50000:
            break
        else :
            print("輸入的數字必須大於0，請重新輸入。")
    except :
        print("輸入的不是有效的整數，請重新輸入。")

count_0 = 0
count_1 = 0
count_2 = 0
for a in range(1,n+1) :
    # print(a)
    if a % 3==0:
        count_0+=1
    elif a % 3==1:
        count_1+=1
    else :
        count_2+=1
    a+=1
print(count_0,count_1,count_2)