p=int(input())
# 如果输入为 0，直接输出 0
if p == 0:
    print('0')
else:
    a=str(p)
    t=len(a)
    t1=[]
    # 跳过末尾的所有0
    while t > 0 and a[t-1] == '0':
        t -= 1

    # 反转剩下的部分
    while t != 0:
        t1.append(a[t-1])
        t -= 1
    print("".join(t1))