def lengthOfLongestSubstring(self, s):
    res=""
    maxx=0
    i=0
    while i<len(s):
        if s[i] not in res:
            res=res+s[i]
        else:
            if s[i]==res[0]:
                res=res[1:]+s[i]
            else:
                idx=res.index(s[i])
                if len(res)>maxx:
                    maxx=len(res)
                res=res[idx+1:]+s[i]
        i=i+1
    if len(res)>maxx:
        maxx=len(res)
    return maxx
