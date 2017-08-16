import re
import urllib.request as request

def urlOpen(url):
    # 设置请求的http头
    head = [("user-agent",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")]


    proxies = {'http': '127.0.0.1:8080'}

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

if __name__ == '__main__':
    url='http://cn-proxy.com/'
    data=urlOpen(url)
    need = re.compile('(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
    iplist=need.findall(data)
    print(iplist)