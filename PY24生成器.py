
def myRev(rev):
    index=len(rev)-1

    while index>-1:
        yield rev[index]
        index-=1


print([i for i in myRev([1,2,3,4])])