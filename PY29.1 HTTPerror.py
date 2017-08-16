import urllib.request as request
import urllib.error

"""常见的url错误处理方法2
httperror有code属性,urlerror没有
httperror是urlerror的子类,所以他们都有reason属性
所以先判断有没有code属性,再判断有没有reason属性

elif的判断是符合第一个就不再匹配第二个了
"""

try:
    '''re是返回404的'''
    re=request.Request('http://www.bilibili.com/hhh')
    '''re0是找不到主机的'''
    re0=request.Request('http://www.lnsdkf.com')
    data=urllib.request.urlopen(re)

except urllib.error.URLError as he:
    if hasattr(he,'code'):
        print('URLError:')
        print('ErrorCode:')
        print(he.code)

    elif hasattr(he,'reason'):
        print('URLError:')
        print('ErrorReason:')
        print(he)



