def isValid(s):
    Pair={'(':')','[':']','{':'}'}  
    sk=[]
    for ch in s:
        if ch in "({[":
            sk.append(ch)
        elif ch in ")]}":
            if len(sk)==0:
                return False
            if Pair[sk.pop()]!=ch:
                return False
        else:
            return False
    if len(sk)==0:
        return True
    return False
