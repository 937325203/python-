"""
def add(a=1,b=2):
    '''可为程序内的参数设定默认值 a=1,b=2
    这样可以防止参数为空出错。
    哦，我是函数文档'''
    return a+b

'''在help内输入函数名称可以打印函数文档'''
help(add)

print(add())
print(add(5,5))
print(add(b=9,a=9))
'也可以这样指明道姓的传'

def exploit(*need,you='you'):
    '''在这里need是一个搜集参数也就是一个可变参数
    在赋值的时候可以随意放多少个参数进去，他会变成一个元组来存储'''
    p=''
    for i in need:
        p=p+i

    print(p+you)

'在传递参数时可以直接放一个串进去，也可以同时给那个单另的参数传'
exploit('i','love')

exploit('i','love',you='LL')
"""

"""
def fuc1(need):
    print(need)
    def fuc2(need1='lg'):
        print(need1)
        need1=need
        print(need1)
    fuc2()
    print(need)
fuc1('hello')
"""

def g(x):
    return x*x

g=lambda x : x*x

print(g(5))

'''第一个参数g是一个函数名称可为空，第二个参数是一个可迭代的对象'''
filter0=filter(g,[1,3,0])
'''filter函数会把传入的可迭代对象的每一个元素带入函数求值，再对求出来的值进行筛选，将值为ture的放入一个可迭代对象返回'''

'''这里使用list将它转换为list'''
print( list(filter0) )

'''第一个参数为一个函数名称，可为空，第二个参数是一个可迭代的对象'''
map0=map(g,[1,3,0])
'''map函数会把传入的可迭代对象的每一个元素带入函数求值，把求出的值放入一个可迭代的对象返回'''
print( list(map0))



