from math import floor # 無條件捨去
total=0
n=int(input())
total=floor(n/12)*50+(n%12)*5
print(total)