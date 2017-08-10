import sys

def reArgv():
    i=0
    key=[]
    argv=sys.argv.pop(0)
    for option in sys.argv:
        op=option.split('=',1)
        key.append(op[1])
        i=i+1

    return key

print(reArgv())
