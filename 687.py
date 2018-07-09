def longestUnivaluePath(p, par=None, cnt=0):
    if not p:
        return cnt
    if not par:
        a=longestUnivaluePath(p.left, p) + longestUnivaluePath(p.right, p)
        b=longestUnivaluePath(p.left)
        c=longestUnivaluePath(p.right)
        return max(a,b,c)
    if p.val!=par.val:
        return cnt
    else:
        left=longestUnivaluePath(p.left, p, cnt+1)
        right=longestUnivaluePath(p.right, p, cnt+1)
        return max(left, right)
