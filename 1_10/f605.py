from statistics import mean
n,d = map(int,input().split(" "))
total = 0
j = 0
m = []
try:
    if 1 <= n <= 100 and 1 <= d <= 100:
        # 讀取輸入，將每個子列表中的元素轉換為整數
        for i in range(n):
            m.append(list(map(int,input().split(" "))))   # 將子列表添加到主列表中
        
        # 打印每行的列表，將數字轉換為字串再用空格分隔
        # for row in m:
        #     print(' '.join(map(str, row)))

            # 進行判斷，並計算每行的結果
            if max(m[i]) - min(m[i]) >= d:
                list_avr = mean(m[i])   # 計算子列表的平均值
                total += list_avr   # 累加到總值中
                j += 1  # 計數器
        # 輸出結果
        print(j,total)
except ValueError:
    print()