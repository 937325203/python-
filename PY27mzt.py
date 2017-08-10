import urllib.request as request
import os

url='http://jandan.net/ooxx/'

def openUrl(url):
    header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    re = request.Request(url, headers=header)
    Response = request.urlopen(re)
    data = Response.read()
    return data

#获得当前页面pageindex
def getUrlInx(httpData):
    a=httpData.find("current-comment-page")+23
    b=httpData.find(']',a)
    urlInx=httpData[a:b]
    return urlInx

#从当前页面取出所有图片地址返回列表
def getPicUrl(httpData):

    picUrlList=[]
    a=httpData.find("img src=")

    #寻找图片url添加到list后
    while a!=-1:
        b=httpData.find(".jpg",a,a+255)
        if b!=-1:
            u='http:'+httpData[a+9:b+4]#拼接图片url
            u=u.replace('mw600','large')
            picUrlList.append(u)
        else:
            b=a+9

        a = httpData.find("img src=",b)

    return picUrlList



#获得当前列表中的所有图片并写入文件中
def getPic(picUrl):
    for url in picUrl:
        na=url.split('/')
        name=na[-1]
        data=openUrl(url)
        file=open(name,'wb')
        file.write(data)

def run(path='/Volumes/小黑2/妹子图前100',pages=100):
    os.mkdir(path)
    os.chdir(path)

    data=openUrl(url)
    data=data.decode('utf-8')
    pageIndex=int(getUrlInx(data))

    for index in range(pages):

        # 获得当前页面url的index
        pageIndex=pageIndex-index
        pageUrl = 'http://jandan.net/ooxx/page-' + str(pageIndex) + '#comments'

        #从当前页面取出所有图片地址返回列表
        data =openUrl(pageUrl)
        httpData=data.decode('utf-8')
        picUrlList=getPicUrl(httpData=httpData)
        # 获得当前列表中的所有图片并写入文件中
        getPic(picUrlList)

if __name__=='__main__':
    run()

