import urllib.request as request
import re
import os
import random

def urlOpen(url,path):
    #过反爬虫
    filePath = path + fileName

    # 设置请求的http头
    head = [("user-agent",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")]

    if os.path.exists(filePath):

        print('文件存在')
        file=open(filePath)
        proxylist=file.readlines()
        rProxy = random.choice(proxylist)
        need = rProxy.replace('\n', '')
        proxies= {'http':need}
        print('使用代理:'+str(proxies))

    else:
        print('文件不存在')
        # 代理ip
        proxies = {'http': '127.0.0.1:8080'}

    # proxies = {'http': '127.0.0.1:8080'}

    # 把代理ip丢给代理助手对象
    proxyHandler = request.ProxyHandler(proxies)
    # 创建自定义Opener
    diyOpener = request.build_opener()
    # 给自定义Opener添加http头，注意这里是给Opener添加了http头
    diyOpener.addheaders = head
    # 给自定义Opener添加代理助手
    diyOpener.add_handler(proxyHandler)
    # 使用urllib.request.install_opener方法安装自定义Opener
    request.install_opener(diyOpener)

    response = diyOpener.open(url,timeout=20)
    data=response.read()
    data=data.decode('UTF-8')

    return data


def ipGet(data):
    findIp=r'<td data-title="IP">((1\d{2}|2[0-5]\d|\d{1,2})\.){3}1\d{2}|2[0-5]\d|\d{1,2}</td>'
    findPort=r'<td data-title="PORT">\d{1,4}'

    ipList=re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',data)
    portList=re.findall(findPort,data)

    ipPort=[]

    for i in range(len(ipList)):
        n=portList[i].split('>',1)
        str=ipList[i]+':'+n[1]+'\n'
        ipPort.append(str)

    return ipPort

def out(iplist,path):

    os.chdir(path)
    file=open(fileName,'a')
    file.writelines(iplist)

def run(page,path):

    url0 = "http://www.kuaidaili.com/free/intr/"

    for i in range(page):
        # 获得url
        i=i+1
        url=url0+str(i)
        print('page'+str(i))

        # 获得网页数据
        HttpData=urlOpen(url,path)

        #爬代理ip和端口
        iplist=ipGet(HttpData)

        #写入文件
        out(iplist,path)


if __name__ == '__main__':

    fileName='ip.txt'
    path='/Users/BigBai/Desktop/'
    page=3
    run(page,path)