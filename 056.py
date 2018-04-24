# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    loc={}
    def insertDict(self,k,lr):
        if k in self.loc.keys():
            self.loc[k]+=lr
        else: self.loc[k]=lr
    def search(self,intervals):
        for i in intervals:
            self.insertDict(i.start,1)
            self.insertDict(i.end,-1)
    def merge(self,intervals):
        self.loc={}
        self.search(intervals)
        sort=sorted(self.loc)
        ret=[]
        sum,bottom=0,0
        for i in sort:
            if sum==0: bottom=i
            sum+=self.loc[i]
            if sum==0:
                ret.append([bottom,i])
        return ret
