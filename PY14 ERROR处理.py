
try:
    print('nihao')
    raise NameError("nnnn")
except (RuntimeError, TypeError, NameError):
    n=NameError.args[0]
    print(n)
