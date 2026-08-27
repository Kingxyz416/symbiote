class Solution(object):
    def maxArea(self, height):
        g=len(height)
        l,r=0,(g-1)
        maxx=0
        while l<r:
            area=min(height[l],height[r])*(r - l)
            maxx=max(maxx,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxx

        