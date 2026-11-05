class Solution(object):
    def missingNumber(self, nums):
        l=len(nums)
        total=l*(l+1)//2
        return total-sum(nums)

        