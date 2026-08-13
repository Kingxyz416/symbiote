import numpy as np
class Solution(object):
    def maximumProduct( nums):
        for i in range (0,len(nums)):
            sig=np.sign(nums[-1])

            if len(nums)==3:
                return nums[-1]*nums[-2]*sig

            elif len(nums)>3:
                
                z=len(nums)
                j=1
                j=j*nums[z-2]*nums[z-1]
                nums.pop()
                nums.pop()
                nums.append(j)
            return nums[-1]*nums[-2]*sig
    a=[1,2,3,4]   
    print(maximumProduct(a))      



                

               
                

        
            


       