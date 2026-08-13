class Solution(object):
    def maximumProduct(self, nums):
        z=sorted(nums)

       
        a= z[0]*z[1]*z[2]
        
        d= z[0]*z[1]*z[-1]
        return max(a,d)
            
            
       
