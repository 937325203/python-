import urllib.request as re
url='http://www.whatismyip.com.tw'

'class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)'

#设置请求的http头
head=[("user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")]

#代理ip
proxies={'http':'110.73.182.12:9000'}

#把代理ip丢给代理助手对象
proxyHandler=re.ProxyHandler(proxies)

#创建自定义Opener
diyOpener=re.build_opener()

#给自定义Opener添加http头，注意这里是给Opener添加了http头
diyOpener.addheaders=head

#给自定义Opener添加代理助手
diyOpener.add_handler(proxyHandler)

print(diyOpener)
print(type(diyOpener))

#使用urllib.request.install_opener方法安装自定义Opener
re.install_opener(diyOpener)

resp=diyOpener.open(url)

hands=resp.getheaders()
date=resp.read().decode('utf-8')
print(date)
