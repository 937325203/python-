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