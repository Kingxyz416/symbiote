class Solution(object):
    def maxProduct(self, n):
        r=[]
        while n:
            t=n%10
            r.append(t)
        d=sorted(r)
        return d[-2]*d[-1]


           
        













