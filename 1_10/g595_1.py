try:
    n=int(input()) # 籬笆數量
    h=list(map(int,input().split())) # 各籬笆數值以列表存取
    total=0 # 需要的籬笆總計

    # 判斷n是否符合範圍3~100以及籬笆數量h是否吻合
    if 3<=n<=100 and len(h)==n:
        # 判斷h是否符合範圍0~100
        if all(0<=x<=100 for x in h):
            # 用迴圈判斷壞掉的籬笆h[i]=0，並且算出修補所需的總高
            for t in range(n):
                if h[t]==0:
                    # 壞在第一個位置的話，直接用第二個的長度
                    if t==0:
                        h[t]=h[t+1]    
                    # 壞在最後位置的話，直接用倒數第二個的長度
                    elif t==n-1:
                        h[t]=h[t-1]
                    # 用前後相比，使用較小的高度
                    else:
                        h[t]=min(h[t-1],h[t+1])
                
                    total+=h[t] # 加上修補的籬笆高度
    print(total)
except ValueError:
    print()




# 精簡版
# try:
#     n = int(input())  # 籬笆數量
#     h = list(map(int, input().split()))  # 各籬笆數值以列表存取
#     total = 0  # 需要的籬笆總計

#     if 3 <= n <= 100 and len(h) == n and all(0 <= x <= 100 for x in h):
#         for t in range(n):
#             if h[t] == 0:
#                 # 根據 t 的位置選擇修補的高度，並加到 total
#                 total += h[t + 1] if t == 0 else h[t - 1] if t == n - 1 else min(h[t - 1], h[t + 1])

#     print(total)

# except ValueError:
#     print()
