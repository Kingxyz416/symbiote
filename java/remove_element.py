class Solution(object):
    def removeElement( nums, val):
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1

        

        return len(nums)    
    c=[0, 1, 2, 2, 3, 0, 4, 2]
    l=2
    print(removeElement( c, l))