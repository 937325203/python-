'''这里有个重要的概念不能混淆：
当你直接写fun的时候是对fun这个方法的对象再操作
比如：
return fun是在返回fun方法

当你写fun()的时候是在调用fun这个方法，要求运行这个方法
return fun()是要求返回fun方法的运行结果
'''

def wai(n):

    '''这里是把传入的n方法进行包装，在_wai方法中爱来白来了一堆。
    就是对方法n进行了装饰'''
    def _wai():
        print("wai:上")
        n()
        print("wai：下")
        return n
        """这里应该返回n()执行后的返回值"""

    '''然后返回_wai这个方法'''
    return _wai

"""这里这个@wai就相当于在后面调用了nei=wai(nei)"""
@wai
def nei():
    i=0
    print(i)
    print("hello")
    return i

"""nei=wai(nei)"""

print(nei)
i=nei()
print(i)


