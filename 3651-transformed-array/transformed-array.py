class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        for i in range(n):
            target_idx=(i+nums[i])%n
            res[i]=nums[target_idx]
        return res
        