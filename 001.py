def twoSum(nums, target):
    for i in range(len(nums)):
        a=target-nums[i]
        if a in nums[i+1:]:
            return [i,nums.index(a,i+1)]
