class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        test=True
        count=1
        if nums[1]<=nums[0]:
            return False
        for i in range(2,len(nums)):
            if nums[i]==nums[i-1]:
                return False
            if test and nums[i]<nums[i-1]:
                count+=1
                test=False
            elif test==False and nums[i]>nums[i-1]:
                count+=1
                test=True
        return count==3
        