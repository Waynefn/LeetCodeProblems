def isHappy(n):
    lst=[]
    while True:
        n=sum(map(lambda x:int(x)**2,str(n)))
        if n==1:
            return True
        elif n in lst:
            return False
        else:
            lst.append(n)
