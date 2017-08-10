f=open('/Users/BigBai/Desktop/hehe1.txt')

mvz=[]
nvz=[]
zhangzhe=[]
pangbai=[]

for each_line in f:
    linelist=each_line.split('：',1)
    name=linelist[0]
    if name=='港女记':
        nvz.append(linelist[1])

    elif name=='江泽民':
        zhangzhe.append(linelist[1])

    elif name=='港男记':
        mvz.append(linelist[1])

    else:
        pangbai.append(name)

fnvz=open('/Users/BigBai/Desktop/fnvz.txt','a')
fzhangzhe=open('/Users/BigBai/Desktop/fzhangzhe.txt','a')
fpangbai=open('/Users/BigBai/Desktop/fpangbai.txt','a')
fmvz=open('/Users/BigBai/Desktop/fmvz.txt','a')

fnvz.writelines(nvz)
fzhangzhe.writelines(zhangzhe)
fpangbai.writelines(pangbai)
fmvz.writelines(mvz)