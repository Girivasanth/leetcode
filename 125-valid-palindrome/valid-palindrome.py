class Solution(object):
    def isPalindrome(self, s):
        s=s.lower().strip()
        r=[i for i in s if i.isalnum()]
        print(r)
        if r[::-1]==r:
            return True
        else:
            return False

        