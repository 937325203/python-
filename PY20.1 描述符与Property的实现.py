class MyProperty:
    def __init__(self,Baget,Baset,Badelete):
        self.Baget=Baget
        self.Baset=Baset
        self.Badelete=Badelete

    """当描述符类的对象被get，set和delete操作的时候就会调用这些方法"""
    """描述符类的牛逼之处就在于它可以调用它所属实例对象，这里的instance就是他所属于的实例对象"""
    def __set__(self, instance, value):
        self.Baset(instance,value)

    def __get__(self, instance, owner):
        return self.Baget(instance)

    def __delete__(self, instance):
        self.Badelete(instance)

class Ba:
    def __init__(self):
        self._x=None

    def set_x(self,value):
        self._x=value

    def get_x(self):
        return self._x

    def delete_x(self):
        del self._x

    """描述符类的实例必须是类属性，不能是实例的属性"""
    """虽然x是类属性，但是这个MyProperty传入参数后是在对实例属性_x在操作，所以可以直接访问x来达到访问_x
    的作用"""
    x=MyProperty(get_x,set_x,delete_x)

b=Ba()
b.x=1
print(b.x)

a=Ba()
a.x=2
print(a.x)