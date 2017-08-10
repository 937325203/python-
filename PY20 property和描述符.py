class PPX:
    def __init__(self):
        self.work="吃"
        self.see="大"

    def getWork(self):
        return self.work

    def setWork(self,value):
        self.work=value

    def delWork(self):
        del self.work

    do=property(getWork,setWork,delWork)

hanlu=PPX()

print(hanlu.do)

hanlu.do='喝'

print(hanlu.do)

print(hanlu.work)

hanlu.work='睡觉'

print(hanlu.work)


