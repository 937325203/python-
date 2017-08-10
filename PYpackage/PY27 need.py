import urllib.request
import http
import sys

#第一个参数菜刀箱子路径
path=sys.argv[1]
#第二个参数可用url路径
kurlpath=sys.argv[2]
#第三个参数不可用url路径
bkurlpath=sys.argv[3]


f=open(path)
url=''
used=['可用']
unused=['不可用']
i=0
j=0

for each_line in f:
    lineArray=each_line.split('|',1)
    url=lineArray[0]
    try:
        response=urllib.request.urlopen(url)
        if (response.status == 200):
            i=i+1
            print(url+ '|' + lineArray[1]+'  '+str(i)+'可用')
            used =url + '|' + lineArray[1]
            kurl = open(kurlpath, 'a')
            kurl.write('\n'+str(i)+'  '+used)
            used=''
    except:
        j=j+1
        print(url +'  '+str(j)+ '不可用')
        unused=url
        bkurl = open(bkurlpath, 'a')
        bkurl.write('\n'+str(j)+'  '+unused)
        unused=''


print('完成')