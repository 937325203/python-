import os

path=input('输入路径:\n')
os.chdir(path)
n_list=os.listdir()


def count(path):

    txt = 0
    pdf = 0
    png = 0
    dir = 0

    for fname in n_list:
        # 扩展名
        extension=os.path.splitext(fname)[1]
        if extension=='.txt':
            txt=txt+1

        if  extension=='.pdf':
            pdf+=1

        if  extension=='.png':
            png+=1

        if  extension=='':
            dir+=1

    print("txt数量:{}\npdf数量{}\npng数量{}\ndir数量{}".format(txt,pdf,png,dir))


def size(path):

    for fname in n_list:

        size=os.path.getsize(fname)
        print("{a}的大小为:{b}字节".format(a=fname,b=size))


count(path)
size(path)