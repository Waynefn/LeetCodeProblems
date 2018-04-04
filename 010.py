class Solution:
    pattern=[]
    asterisk=[]
    def changePattern(self,p):
        i=0
        p+='$'
        while i<len(p)-1:
            self.pattern.append(p[i])
            if  p[i+1]=='*':
                self.asterisk.append(1)
                i+=2
            else:
                self.asterisk.append(0)
                i+=1
    def shouldRecovery(self,slen,si,pi,stacklen):
        ##success 0
        ##failed -1
        ##recovery 1
        if si==slen:
            for i in self.asterisk[pi:]:
                if i==0:
                    if stacklen==0: return -1
                    else: return 1
            return 0
        else:
            if stacklen==0:
                return -1
            return 1
    def checkMatch(self, s):
        si,pi=0,0
        stack=[]
        
        p=self.pattern
        a=self.asterisk
        while True:
            #print("%d(%s)<-%d(%s)(*=%d),stk:"%(si,s[si],pi,p[pi],a[pi]),stack)
            if s[si]==p[pi] or p[pi]=='.':
                if a[pi]==0:
                    si+=1
                    pi+=1
                else:
                    if pi+1<len(p):
                        stack.append([si,pi+1])
                    si+=1
                    
            else:
                if a[pi]==0:
                    if len(stack)==0: return False
                    else:
                        #print("recovery")
                        si,pi=stack.pop()
                else:
                    pi+=1
            if si==len(s) or pi==len(p):
                ret=self.shouldRecovery(len(s),si,pi,len(stack))
                if ret==0: return True
                elif ret==-1: return False
                #print("recovery")
                si,pi=stack.pop()
    def isMatch(self, s, p):
        self.pattern=[]
        self.asterisk=[]
        self.changePattern(p)
        if len(s)==0 or len(p)==0:
            if len(s)==0:
                return self.shouldRecovery(0,0,0,0)==0
            return False
        return self.checkMatch(s)
