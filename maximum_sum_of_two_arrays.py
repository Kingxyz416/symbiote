class Solution(object):
    def maxProduct(self, nums1):
        nums1=sorted(nums1)
        n=len(nums1)
        
        x=(nums1[n-1]-1)*(nums1[n-2]-1)
        return x 

