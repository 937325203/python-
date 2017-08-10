class people:
    def InstanceFun(self):
        print(self)


    @classmethod
    def classFun(cls):
        print(cls)

    @staticmethod
    def staticFun():
        print("说啥好呢...")

"""实例对象可调用类方法"""
liuting=people()

"""实例方法"""
liuting.InstanceFun()
"""类方法"""
liuting.classFun()
"""静态方法"""
liuting.staticFun()

"""类对象不能调用实例方法"""
#people.InstanceFun()
people.staticFun()
people.classFun()
"""他们都可以调用静态方法"""

class a:
    a='h'

need=a()
print(need.a)
a.a='w'
need0=a()
print(need0.a)

