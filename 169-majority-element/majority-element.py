class Solution(object):
    def majorityElement(self, nums):
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        m=0
        ans=0
        for i,j in dic.items():
            if j>m:
                m=j
                ans=i
        return ans

        