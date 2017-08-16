#re包用于正则表达式
import re

#search函数,从第二个字符串中寻找第一个字符串第一次出现的位置
print(re.search(r'lulu','i love lulu'))

#.代表任意一个字符
print(re.search(r'i.l','i love lulu'))

#\.代表.
print(re.search(r'\.','i love. lulu'))

#\d代表一个数字
print(re.search(r'\d','i love lu2lu'))

#[]创建字符类,只要在[]中,就会匹配到
#正则表达式是大小写敏感的
print(re.search(r'[aeiou]','i love you'))

#可使用 - 代表一个区间
print(re.search(r'[k-n]','i love you lulu'))

#{}代表前面部分的重复次数.下面这个就是数字三次就可以匹配到
print(re.search(r'\d{3}','abcdefg999'))

#可以给{}一个范围,代表重复次数的范围
print(re.search(r'\d{3,9}','abcdefg9998679'))

#可用|代表或
print(re.search(r'\d{3,9}|.{3,5}','abcdefg9998679'))

#尝试匹配0~255
print(re.search(r'(1\d{2}|2[0-5]\d|\d{1,2}),','110,'))

#尝试匹配ip地址
print(re.search(r'((1\d{2}|2[0-5]\d|\d{1,2}),){3}1\d{2}|2[0-5]\d|\d{1,2}','1,10,123,115'))

# \
# 如果在反斜杠后边紧跟着一个元字符，那么元字符的“特殊功能”不会被触发
# 反斜杠后边跟元字符去除特殊功能，反斜杠后边跟普通字符实现特殊功能
print(re.findall(r'\.+','....'))

# \d 匹配任何十进制数字[0-9]
print(re.findall(r'\d','abc89d'))

# \D 匹配任何非十进制数字相当于类[^0-9]
print(re.findall(r'\D','abc89d'))

# \s 匹配任何空白字符,相当于类 [ \t\n\r\f\v]
print(re.findall(r'\s','ab c8\n9d'))

# \S 与s相反,匹配任何非空白字符,相当于类 [^\t\n\r\f\v]
print(re.findall(r'\S','ab c8\n9d'))

# \b匹配单词的开始或结束 \B 与\b相反
# 他匹配的单词边界,符号都算单词边界,但是_不算
print(re.findall(r'\bhello\b','hello 1world hello'))



# \w
# \w 匹配任何字符。如果正则表达式以字节的形式表示，这相当于字符类 [a-zA-Z0-9_]；如果正则表达式是一个字符串，\w 会匹配所有 Unicode 数据库（unicodedata 模块提供）中标记为字母的字符。你可以在编译正则表达式的时候，通过提供 re.ASCII 表示进一步限制 \w 的定义。
print(re.findall(r'\w','hello 1world \n hello'))

# \W 和\w相反
print(re.findall(r'\W','hello 1world hello\n'))

# * ={0,} 匹配0次到多次
# 输出['', '', 'll', '', ''] 因为''为空,0即为空,可匹配到
print(re.findall(r'l*','hello'))
print(re.findall(r'l{0,}','hello'))

# + ={1,} 匹配1次到多次
print(re.findall(r'l+','hello'))

# ? ={0,1} 匹配0次到一次
# ['', '', 'l', 'l', '', ''] 因为''为空,0即为空,可匹配到
print(re.findall(r'l?','hello'))

# []字符类
# 被包含在里面的元字符都会失去特殊功能
# \不是,\在字符类中代表转义符号,例如\n
# ^也不是,^代表取反
# \b表示退格
print(re.findall(r'[^.\d]','hello.123'))

# 贪婪模式
# 默认为贪婪模式,即在可能的情况下尽可能多的匹配字符
# 去除贪婪模式
# 在表示重复的符号后面加上?即可
print(re.search(r'<.+>','<html><head>helloword</html>'))
print(re.search(r'<.+?>','<html><head>helloword</html>'))


# 零宽断言
# 下面的这几个都是零宽断言

# ^ 只能放在开头,匹配开头=\A
print(re.findall(r'p','pkasjdpflpk'))
print(re.findall(r'^p','pkasjdpflpk'))

# $ 只能放在开头,匹配开头=\B
print(re.findall(r'pk','pkasjdpflpk'))
print(re.findall(r'pk$','pkasjdpflpk'))


# findall
