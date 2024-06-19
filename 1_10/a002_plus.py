# 用 split() 把字符串以空白標誌分割成多個字串符，若想用逗號圍間隔標誌，可以用split(',')
a,b=map(int,input("輸入a,b空格隔開:").split())
total=int(a+b)
print(total)