class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost=0
        first=nums[0]
        cost+=first
        nums.sort()
        if nums[0]==first:
            cost+=nums[1]+nums[2]
        elif nums[1]==first:
            cost+=nums[0]+nums[2]
        else:
            cost+=nums[0]+nums[1]
        return cost        