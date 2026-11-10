class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum<0 or sum>num*9:
            return ""
        result=""
        while num>0:
            if sum>=9:
                digit=9
            else:
                digit=sum
            result+=str(digit)
            sum=sum-digit
            num-=1
        return result
        