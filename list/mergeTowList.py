# 合并两个有序数组
# 输入 nums1 = [1,2,3,0,0,0] , m=3, nums2 = [2,5,6], n=3
# 输出 [1,2,3,3,5,6]
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        size = len(nums1) - 1
        p1 = m - 1
        p2 = n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[size] = nums1[p1]
                p1 = p1 - 1
            else:
                nums1[size] = nums2[p2]
                p2 = p2 - 1
            size = size - 1
