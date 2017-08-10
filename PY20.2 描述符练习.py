class hua:
    def __init__(self,set,get):
        self.set=set
        self.get=get

    def __set__(self, instance, value):
        self.set(instance,value)

    def __get__(self, instance, owner):
        return self.get(instance)*1.8+32

class she:
    def __init__(self,set,get):
        self.set=set
        self.get=get

    def __set__(self, instance, value):
        self.set(instance,value)

    def __get__(self, instance, owner):
        return self.get(instance)


class tem:
    def __init__(self,temp):
        self._temp=temp

    def set_temp(self,value):
        self._temp=value

    def get_temp(self):
        return self._temp

    Ftemp=hua(set_temp,get_temp)
    Ctemp=she(set_temp,get_temp)



t=tem(20)
print(t.Ftemp)
print(t.Ctemp)