class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        rev=x[::-1]
        print(rev)
        if rev==x and x.isdigit():
            return True
        else:
            return False
        