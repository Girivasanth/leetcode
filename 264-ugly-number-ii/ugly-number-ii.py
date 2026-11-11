class Solution(object):
    def nthUglyNumber(self, n):
        l=[0]*n
        l[0]=1
        p2=0
        p3=0
        p5=0
        for i in range(1,n):
            next2=l[p2]*2
            next3=l[p3]*3
            next5=l[p5]*5
            nextugly=min(next2,next3,next5)
            l[i]=nextugly
            if next2==nextugly:
                p2+=1
            if next3==nextugly:
                p3+=1
            if next5==nextugly:
                p5+=1
        return l[n-1]
            