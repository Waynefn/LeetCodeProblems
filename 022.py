class Solution:
    comb=[]
    def parenth(self,s,num,n):
        if n==0:
            if num==0:
                self.comb.append(s)
            return
        if num>=1:
            self.parenth(s+')',num-1,n-1)
        self.parenth(s+'(',num+1,n-1)
        
    def generateParenthesis(self, n):
        self.comb=[]
        self.parenth("(",1,2*n-1)
        return self.comb
