class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        def GCD(x,y):
            while y!=0:
                temp=y
                y=x%y
                x=temp
            return x
        def LCM(x,y):
            return (x/GCD(x,y))*y
        ab=LCM(a,b)
        bc=LCM(b,c)
        ac=LCM(a,c)
        abc=LCM(ab,c)
        low=1
        high=2*(10**9)
        while low<high:
            mid=(low+high)//2
            count=(mid/a)+(mid/b)+(mid/c)-(mid/ab)-(mid/bc)-(mid/ac)+(mid/abc)
            if count<n:
                low=mid+1
            else:
                high=mid
        return low
        