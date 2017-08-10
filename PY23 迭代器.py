class fan:
    def __init__(self,data):
        self.data=data
        self.index=len(data)-1

    def __iter__(self):
        return self

    def __next__(self):

        if self.index!=-1:
            i=self.index
            self.index=self.index-1
            return self.data[i]

        else:
            raise StopIteration


i=[1,2,3,4,5]
I=fan(i)
while True:
    try:
        print(next(I))
    except StopIteration:
        print("循环完毕，捕捉到StopIteration错误")
        break