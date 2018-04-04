def maxArea(height):
    lid,rid=0,len(height)-1
    lv, rv=height[lid], height[rid]
    maxVol=min(lv,rv)*(rid-lid)
    while lid<rid:
        if lv<rv: lid+=1
        elif lv>rv: rid-=1
        else: lid,rid=lid+1,rid-1
        lv, rv=height[lid], height[rid]
        maxVol=max(maxVol,min(lv,rv)*(rid-lid))
    return maxVol
