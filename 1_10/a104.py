while True:
    try:
        new_m=[]
        # 嘗試讀取第一行的整數 n
        n=int(input())
        if 1<=n<=1000:
            try:
                # 嘗試讀取第二行的數字列表
                m=list(map(int,input().split()))
                if len(m)==n:
                    for i in m:
                        if i>=0:
                            new_m.append(i)
                    new_m.sort()
                    print(" ".join(map(str,new_m)))
            except EOFError:
                break
    except EOFError:
        break
    
#精簡版
# while True:
#     try:
#         n = int(input())  # 讀取第一行的 n
#         m = list(map(int, input().split()))  # 讀取第二行的數字列表
        
#         if len(m) == n and 1 <= n <= 1000:  # 檢查 n 和數字列表的長度是否匹配
#             new_m = sorted(x for x in m if x >= 0)  # 過濾非負數並排序
#             print(" ".join(map(str, new_m)))
    
#     except (EOFError, ValueError):  # 捕捉 EOF 或無效輸入後退出
#         break

########筆記##########
# squares = [x * x for x in [1, 2, 3, 4, 5]]
# 這段程式碼的含義是：

# 遍歷列表 [1, 2, 3, 4, 5]，每個元素都會被存入變量 x 中。
# x * x （表達式部分）是對每個元素進行平方操作。
# 結果是生成一個新的列表 [1, 4, 9, 16, 25]。