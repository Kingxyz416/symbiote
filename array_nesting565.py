class Solution(object):
    def arrayNesting(self, nums):
        t=[]
        for i in range(0,len(nums)):
            j=i
            k=[]
            while True:
                x=nums[i]
                
                k.append(x)
                i=x
                if i==j:
                    break
                else:
                    continue
                
            t.append(len(k))
        return max(t)
    
            

            
            
     




        
        