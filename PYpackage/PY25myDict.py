class myDict(dict):
    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)

    def __setattr__(self, key, value):
        self[key]=value

    def __getattribute__(self, item):
        try:
            return self[item]

        #试图捕获KeyError
        except (KeyError):
            print("你好呀，乱写参数是不对的")
            pass

    def __getattr__(self, item):
        print(item+"不存在")

def ceshi():
    n=myDict(b="hello",c="niubi")
    print(n,n.b)
    n.b="999"
    print(n.b)

if __name__=="__main__":
    ceshi()