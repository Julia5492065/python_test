from math import floor
total=0
n=int(input())
if n % 12 ==0:
    total=floor(n/12)*50
else :
    total=floor(n/12)*50+(n%12)*5
print(total)