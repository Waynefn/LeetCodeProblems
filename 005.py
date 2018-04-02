class Solution:
    def getOppo(self,s,mid,right,hasMid):
        if hasMid:
            left = 2 * mid - right
        else:
            left= mid-right
        if left >= 0 and right>left:
            return s[left]
        return ''

    def longestPalindrome(self, s):
        l = s[0]
        mid1 = 0
        mid2 = 1
        i=1
        while i<len(s):
            if s[i]==self.getOppo(s,mid2,i,False):
                t=s[mid2-i:i+1]
                if len(t) > len(l):
                    l = t
                i+=1
            else:
                mid2=mid2+2
                i=(mid2+1)//2
        i=0
        while i<len(s):
            if s[i] == self.getOppo(s,mid1,i,True):
                t = s[2 * mid1 - i:i + 1]
                if len(t) > len(l):
                    l = t
                i+=1
            else:
                mid1+=1
                i=mid1+1
        return l
