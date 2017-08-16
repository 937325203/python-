import urllib.request as request
import urllib.error

"""常见的url错误处理方法1
注意httperror要放在 urlerror前面
因为httperror是urlerror的子类,放到后面他就捕捉不到错误了

当能找到主机但是找不到页面的时候是httperror
直接找不到主机的时候就是一个urlerror
"""

try:
    re=request.Request('http://www.bilibili.com/hhh')
    re0=request.Request('http://www.lnsdkf.com')
    data=urllib.request.urlopen(re)

except urllib.error.HTTPError as he:

    print('httperror:')
    #httperror的方法
    print(he)
    print(he.headers)
    print(he.reason)
    print(he.read())


except urllib.error.URLError as e:
    print('urlerror:')
    print(e)