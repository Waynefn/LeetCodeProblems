def maxSubArray(nums):

    for i in range(1,len(nums)):
        nums[i]=max(nums[i]+nums[i-1],nums[i])
    return max(nums)
