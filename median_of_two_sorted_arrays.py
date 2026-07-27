class solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        self=[]
        sum=0
        n=len(nums1)
        m=len(nums2)
        for i in range(0,n):
            sum+=nums1[i]
            self.append(i)

        for j in range(0,m):
            sum+=nums2[j]
            self.append(j)
        median= sum/(m+n)
        self=sorted(self)


