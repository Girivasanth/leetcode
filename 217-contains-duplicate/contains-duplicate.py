class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}

        for i in nums:
            if i in dic:
                return True
            dic[i] = 1

        return False