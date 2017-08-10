import random

#给出随机答案
a=0
b=5
need=random.randint(a,b)

#欢迎界面
print ('--------------------欢迎----------------------')
print(str(a)+'到'+str(b)+'你猜我在想几？：\n')
#输入
temp=input()

#判断输入
while not temp.isdigit():#isdigit方法检测字符串内是否全部为数字
    print('不是数字，请重新输入\n')
    temp=input()
guss=int(temp)

#判断答案
while guss!= need:
    print('没猜对')

    if guss>=need:
        print('大了')
    else:
        print('小了')

    print('重新输入：\n')
    temp=input()

    while not temp.isdigit():  # isdigit方法检测字符串内是否全部为数字
        print('不是数字，请重新输入\n')
        temp = input()

    guss=int(temp)


print('恭喜你猜对啦~~~')
print('游戏结束~~~')