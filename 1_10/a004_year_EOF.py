#EOF特殊用法  https://hackmd.io/@s10109670/Sko5kJSY_

while True:
    try:
        y = int(input())

        if y % 400==0:
            print("閏年")
        elif y % 4 ==0 and y % 100!=0 :
            print("閏年")
        else:
           print("平年")
    
    except EOFError:
        break


# 解法2
# while True: 
#     try: 
#         year = int(input()) 
#         if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): 
#             print("閏年") 
#         else: 
#             print("平年") 
#     except EOFError: 
#         break

 