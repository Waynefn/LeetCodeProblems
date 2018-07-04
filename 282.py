class Solution(object):
    def helper(self,idx,expr):
        if idx==len(self.nums):
            if eval(expr)==self.target:  #eval() is too slow 
                self.ret.append(expr)
            return
        if expr[-1]!='0':
            self.helper(idx+1,expr+self.nums[idx])
        if expr[-1] not in "+-*":
            for op in "+-*":
                self.helper(idx,expr+op)

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if num=='': return []
        self.ret=[]
        self.target=target
        self.nums=num[1:]
        self.helper(0,num[0])
        return self.ret
