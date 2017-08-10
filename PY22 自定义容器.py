class guo:
    def __init__(self,*args):
        #self.count=dict.fromkeys(range(len(args)),0)
        self.count=[0]*len(args)
        self.lst=list(args)


    """定义作为容器的方法"""
    def __len__(self):
        return len(self.lst)

    def __getitem__(self, item):
        self.count[item]=self.count[item]+1
        return self.lst[item]

    def __setitem__(self, key, value):
        self.count[key]=0
        self.lst[key]=value

    def __delitem__(self, key):
        del self.count[key]
        del self.lst[key]


    """容器应该有的方法"""
    def __reversed__(self):
        return list(reversed(self.lst))

    def __iter__(self):
        self.iter=iter(self.lst)
        return  self.iter

    def __next__(self):
        return next(self.iter)

    def append(self,value):
        self.lst.append(value)
        self.count.append(0)

    def pop(self,index=-1):
        self.count.pop(index)
        return self.lst.pop(index)

    def remove(self,obj):
        """找到匹配项的索引位置"""
        index=self.lst.index(obj)
        """移除匹配项"""
        self.lst.remove(obj)
        """从计数列表中移除匹配项的计数器"""
        del self.count[index]

    def insert(self,index,obj):
        self.lst.insert(index,obj)
        self.count.insert(index,0)


    def clear(self):
        self.count.clear()
        self.lst.clear()

    """自定义的特色方法"""
    def counter(self,index):
        return self.count[index]



g=guo("nihao","hhh","ninnn")
print(g,g.__dict__,)
g[0]
g[0]
g[2]
"""print(g[1])
print(g,g.__dict__)
del g[0]
print(g,g.__dict__)
g[0]="jiji"
print(len(g))
print(g,g.__dict__)
print(reversed(g))"""

g.remove('hhh')
print(g,g.__dict__,)

n=iter(g)

for each in n:
    print(each)
