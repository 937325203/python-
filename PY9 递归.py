
def tu(n):

    if (n==1 or n==2):
        return 1

    elif (n>2):

        return tu(n-1)+tu(n-2)

n=int(input('输入：'))

print(tu(n))
