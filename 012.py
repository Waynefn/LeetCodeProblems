def intToRoman(num):
    Table={0:'',1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
    ref=1000
    roma=''
    while ref>=1:
        k=int(num/ref)
        if k>0:
            if k<=3:
                roma+=Table[ref]*k
            elif k==4:
                roma+=Table[ref]+Table[ref*5]
            elif k<=8:
                roma+=Table[ref*5]+Table[ref]*(k-5)
            elif k<10:
                roma+=Table[ref]+Table[ref*10]
        num-=k*ref
        ref/=10
    return roma
    
