class Solution(object):
    def removeDuplicates(nums):
        new=sorted(nums)
        j=1
        while j<len(new):
            if new[j]==new[j-1]:
                new.pop(j)
            else:
                j+=1
        
        return len(new)


   









