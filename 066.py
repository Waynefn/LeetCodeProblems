def plusOne(digits):
    carry=1
    for i in range(len(digits)-1,-1,-1):
        sm=digits[i]+carry
        print(sm)
        carry=1 if sm>9 else 0
        digits[i]=sm%10
        if carry==0:
            return digits
    if carry!=0:
        digits=[1]+digits
    return digits
