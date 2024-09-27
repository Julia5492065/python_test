a, b = map(int,input().split(" "))
n = int(input())
count_both = 0

if 1 <= n <= 100 and 1 <= a <= 100 and 1 <= b <= 100:
    for i in range(n):
        calc_a = 0
        calc_b = 0
        row = list(map(int,input().split(" ")))  # 將輸入的值添加到子列表
        
        if row[len(row)-1]==0:  # 確認row 列表中的最後一個值是否為0
            for j in range(len(row)):  # 迴圈遍歷 row 列表中的每一個子列表
                if 0 < abs(row[j]) <= 100:  # 如果該元素的絕對值小於等於 100
                    if abs(row[j]) == a:  # 如果該元素的絕對值等於 a(找出a商品)
                        calc_a += row[j]
                    if abs(row[j]) == b:  # 如果該元素的絕對值等於 a(找出a商品)
                        calc_b += row[j]

            # 如果找到的 a 和 b 都大於 0，則計數            
            if calc_a > 0 and calc_b > 0:
                count_both += 1

            # print(calc_a, calc_b,"~")
    print(count_both)



############GPT簡化版###########
# a, b = map(int, input().split())
# n = int(input())
# count_both = 0

# if 1 <= n <= 100 and 1 <= a <= 100 and 1 <= b <= 100:
#     for _ in range(n):
#         calc_a, calc_b = 0, 0
#         row = list(map(int, input().split()))
        
#         if row[-1] == 0:  # 用負索引檢查最後一個元素是否為 0
#             for val in row:
#                 if 0 < abs(val) <= 100:  # 如果該元素的絕對值小於等於 100
#                     if abs(val) == a:
#                         calc_a += val
#                     if abs(val) == b:
#                         calc_b += val

#             # 如果找到的 a 和 b 都大於 0，則計數
#             if calc_a > 0 and calc_b > 0:
#                 count_both += 1

#     print(count_both)
