while True:
    user_input = input("請輸入一個大於0, 並且小於10000的整數（輸入0退出）: ")
    try:
        n = int(user_input)
        if n == 0:
            break
        elif n > 0 and n <= 10000:
            t=[]
            n-=1
            while n > 0:
                if n % 7 != 0:
                    t.insert(0,n)
                n -= 1
            print(" ".join(map(str, t)))
        else:
            print("請輸入大於0,並且小於10000的整數: ")
    except ValueError:
            print("請輸入整數: ")


# #簡潔寫法
# while True:
#     user_input = input("請輸入一個大於0, 並且小於10000的整數（輸入0退出）: ")
#     try:
#         n = int(user_input)
#         if n == 0:
#             break
#         elif 0 < n <= 10000:
#             t = [str(i) for i in range(1, n) if i % 7 != 0]
#             print(" ".join(t))
#         else:
#             print("請輸入大於0, 並且小於10000的整數")
#     except ValueError:
#         print("請輸入有效的整數")
