class People():
    def __init__(self,h='0',w='0'):
        self.h=h#这两步就会调用下面的两个方法
        self.w=w

    """定义当属性被设置时的行为"""
    def __setattr__(self, key, value):
        print("设置变量"+key+"为"+value)
        """注意在setattr方法中对属性赋值不能直接self.属性->循环调用"""
        super(People,self).__setattr__(key,value)#不写这句super就赋值不上去了2333，h直接不存在


    """定义当属性被访问时的行为"""
    def __getattribute__(self, item):
        print("被访问"+item)
        return super(People,self).__getattribute__(item)#不写这句return就得不到这个值了，得到个None


    """定义不存在的属性被访问时的行为"""
    def __getattr__(self, item):
        print("企图访问"+item)
        print(item+"不存在")

    def wang(self,speak):
        self.speak=speak
        print(self.speak)

hanlu=People('165','57')

print(hanlu.h)

hanlu.wang("nihao")
print(People.mro())