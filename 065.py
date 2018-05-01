# It isn't the expected answer!
def isNumber(s):
    try:
        i=float(s)
    except Exception:
        return False
    return True
