class Solution(object):
    def sortedSquares(self, nums):
        k=[]
        for i in range (0,len(nums)):
            j=(nums[i])**2
            k.append(j)
        return sorted(k)

       