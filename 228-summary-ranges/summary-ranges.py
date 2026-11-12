class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        result = []
        start = nums[0]
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                prev = nums[i]
            else:
                if start == prev:
                    result.append(str(start))
                else:
                   result.append("{}->{}".format(start, prev))
                start = nums[i]
                prev = nums[i]

        if start == prev:
            result.append(str(start))
        else:
            result.append("{}->{}".format(start, prev))

        return result