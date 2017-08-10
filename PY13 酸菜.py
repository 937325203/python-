import pickle
import os

list=['i','love','u','\n','thank','you']

#创建文件,'wb'代表打开并且写入二进制数据
pickle_file=open('/Users/BigBai/Desktop/list.LU','wb')

#向这个文件中写入,dump
pickle.dump(list,pickle_file)

#关闭文件
pickle_file.close()

#打开文件,'rb'代表打开并且以二进制读出数据
rpickle_file=open('/Users/BigBai/Desktop/list.LU','rb')

list0=pickle.load(rpickle_file)

print(list0)