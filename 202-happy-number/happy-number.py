class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            s = str(n)
            result = 0

            for i in s:
                result += int(i) ** 2

            n = result

        return True