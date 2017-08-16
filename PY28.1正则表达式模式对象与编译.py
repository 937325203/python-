import re

# 对正则表达式进行编译,第二个参数是编译模式
# 返回一个模式对象
p=re.compile('(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')

#模式对象的使用与直接进行匹配类似,只是不用传入正则表达试而已
print(re.search('(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])','192.168.0.1'))
print(p.search('192.168.0.1'))

# 编译标志
# re.S
# .代表匹配任意单个字符，但是一般情况下\n \t字符却匹配不到。匹配时候加上re.S编译标志即可解决问题。
str='ht\nkjnit'
print(re.findall('t..',str,re.S))

# re.I
# re.IGNORECASE的缩写，此编译标志代表，匹配时候忽视字母大小写
str0='top Top tOp'
print(re.findall('top',str0,re.I))

# re.M
# re.MULTILINE的缩写：多行匹配，影响 ^ 和 $
r1 = r"^hello|good$"
s = """
hello world
hello python
very good
"""

#在一个字符串有多行的时候
print (re.findall(r1, s)) #不加re.M之匹配第一行
print ("#"*20)
print (re.findall(r1, s, re.M)) #加了之后，匹配所有的行

# re.X
# re.VERBOSE的简写，能够使用REs的verbose状态，使之正则表达式更加清晰。
#匹配一个电话号码:0570-1234567
res = r"""
\d{3,4}
-?
\d{6,7} 
"""
#res = r"\d{3,4}-?{6,7}" 如果这样的话，匹配不需要加re.X
print(re.findall(res, "0570-1234567"))
print("#"*20)
print(re.findall(res, "0570-1234567", re.X))
