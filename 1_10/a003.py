m, d=map(int,input("請輸入月 日: ").split()) #m, d此時都是int型態，輸入用空格隔開
s = ( m * 2 + d ) % 3
##方法1
# if s==0:
#     print("普通")
# elif s==1:
#     print("吉")
# elif s==2:
#     print("大吉")

#方法2
def numbers_to_strings(s):
    switcher = {0:'普通', 1:'吉', 2:'大吉'}
    return switcher.get(s, 'nothing')
print(numbers_to_strings(s))