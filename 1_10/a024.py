#暴力法
# a,b=map(int,input().split())
# t1=[]
# t2=[]
# for i in range(1,a+1):
#     if a % i==0:
#         t1.append(i)
# print(" ".join(map(str, t1)))
# for i in range(1,b+1):
#     if b % i==0:
#         t2.append(i)
# print(" ".join(map(str, t2)))

# #使用交集
# set_t=set(t1)&set(t2)
# t=max(set_t)
# print("最大公因數: ",t)



#精簡暴力法
# a,b=map(int,input().split())
# if a>b:
#     c=b
# else:
#     c=a
# for k in range(c,2,-1):
#     if a % k==0 and b % k==0:
#         print(k)
#         break



#輾轉相除法
# a,b=map(int,input().split())
# # if a<b:
# #     c=a
# #     a=b
# #     b=c
# while a % b!=0:
#     c=a
#     a=b
#     b=c % a
#     #可簡化成 a,b = b,a % b
# print(b)



#輾轉相除法_套公式
# import math
# a,b=map(int,input().split())
# print(math.gcd(a,b))



#輾轉相除法_函式
a,b=map(int,input().split())
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)
print(GCD(a,b))
