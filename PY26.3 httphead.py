import urllib.request as request

url='http://www.whatismyip.com.tw'

'方法1：'
headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
re=request.Request(url,headers=headers)

'方法2：'
# re=request.Request(url)
# re.add_header("user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
# print(re.headers)
# response=request.urlopen(re)
