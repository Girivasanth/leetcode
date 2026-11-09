class Solution(object):
    def containsDuplicate(self, nums):
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        val=dic.values()
        print(val)
        m=1
        for j in val:
            if j>m:
                return True
        return False      