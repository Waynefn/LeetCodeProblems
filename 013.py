class Solution(object):
    Table={'*':0,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    def read(self,rm):
        last='*'
        cnt=1
        ret=[]
        for i in rm:
            if i == last:
                cnt+=1
            else:
                ret.append(cnt*self.Table[last])
                last=i
                cnt=1
        ret.append(cnt*self.Table[last])
        return ret[1:]
    def count(self,rml):
        ret=0
        for i in range(1,len(rml)):
            if rml[i]>rml[i-1]:           
                ret-=rml[i-1]      
            else:
                ret+=rml[i-1]
        return ret+rml[-1]
    def romanToInt(self, s):
        return self.count(self.read(s))
        
        
