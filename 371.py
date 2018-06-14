def getSum(a,b):
    if b>a:
        return add(b,a)  # a+b == b+a
    if abs(b)>abs(a):
        return add(~add(add(~b,1),add(~a,1)),1)  #  a+b ==  -(-b - a)
    c=0 #carry
    r=0 #result
    i=0 #bit number

    for i in range(0,len("{:b}00".format(a))): # get bit length of a<<2
        x=((1<<i)&a)>>i # use a full adder method
        y=((1<<i)&b)>>i
        r=r|((x^y^c)<<i)
        c=(x&y)|(c&(x^y))
    return r
