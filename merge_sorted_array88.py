class Solution(object):
    def merge(self, nums1, m, nums2, n):
        mer = nums1[:m] + nums2[:n]
        nums1[:m + n] = sorted(mer)
    