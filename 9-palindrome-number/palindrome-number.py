class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        rev=x[::-1]
        if rev==x and x.isdigit():
            return True
        else:
            return False
        