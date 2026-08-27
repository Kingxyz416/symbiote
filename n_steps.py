import math
class Solution(object):
    def climbStairs(self, n):
        r=math.factorial(n)
        x,y=1,2
        t=math.factorial(r-x)
        e=(math.factorial(x))*t
        o=t/e
        j=math.factorial(r-y)
        q=(math.factorial(y))*j
        s=j/q
        return s+o
        
        
        
        