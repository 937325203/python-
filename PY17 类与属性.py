class people():

    "在这里的这个age1,sentence1是局部变量,self.age和self.sentence是类的属性"
    def __init__(self,age1='10',sentence1='hello'):
        self.age=age1
        self.sentence=sentence1

    def sepak(self):
        print(self.sentence+self.age)

    def eat(self,food='面'):
        print(food)

me=people(age1='22',sentence1='bys')
me.sepak()

