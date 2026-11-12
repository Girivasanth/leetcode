class Solution(object):
    def canWinNim(self, n):
        if 1<=n<=3:
            return True
        elif n%4==0:
            return False
        else:
            return True
        