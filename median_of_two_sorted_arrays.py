class Solution(object):
    def findMedianSortedArrays(arr,nums1,nums2):
        arr=[]
        total=0
        n=len(nums1)
        m=len(nums2)
        for i in range(0,n):
            total+=nums1[i]
            arr.append(nums1[i])

        for j in range(0,m):
            total+=nums2[j]
            arr.append(nums2[j])
        
        arr=sorted(arr)
        l=len(arr)
        if l % 2 == 1:
            median = arr[l//2]
        else:
            median = (arr[l//2 - 1] + arr[l//2]) / 2.0
        return median 

       

    


