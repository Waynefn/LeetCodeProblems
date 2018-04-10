def letterCombinations(digits):
    ret=['']
    ndict={'1':[''],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
           '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z'],'0':['']}
    for i in digits:
        last=len(ret[0])
        now=len(ndict[i])
        tret=[]
        for j in range(now):
            t=list(map(lambda x:x+ndict[i][j],ret))
            tret+=t
        ret=tret
    return ret if ret!=[''] else []
