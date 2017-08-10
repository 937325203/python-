from urllib import request
import os

path="/Users/BigBai/Desktop/httpPage.html"
url="https://www.baidu.com"

#n是一个 HTTPResponse 对象
n=request.urlopen(url)
print(type(n))

#获得描述符
fileno=n.fileno()
print("描述符:\n"+str(fileno))

#获得响应符msg：比如OK
print("msg:%s"%(n.msg))

#获得HTTP版本
#11->http1.1 10->http1.0
print("version:%s"%(n.version))

#获得状态码int类型
nn=type(n.status)
print(nn,n.status)

#获得文件头列表
headList=n.getheaders()
print("文件头列表:")
print(headList)

#获得指定的头
Date=n.getheader("Date")
print(Date)

#读取并返回响应体
date=n.read()
# date=date.decode('utf-8')
#print("-----------------------以下是响应体------------------"+date)

#没搞懂。。。
# date=n.readinto(20)
# print(str(date))
#print("-----------------------以下是响应体------------------"+date)

#文件操作

#打开文件 a代表追加
txt=open(path,"ab")

#txt.writelines("\n-------------------------------------------------------------\n")
#写入文件
txt.write(date)

#打印头
# for ob1,ob2 in headList:
#     st=ob1+":"+ob2+"\n"
#     print(st)
#     txt.writelines(st)

#分割线

#txt.writelines("\n-------------------------------------------------------------\n")
txt.close()
