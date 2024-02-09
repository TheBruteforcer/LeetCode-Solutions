# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = nums1[:m]
        y = nums2[:n]
        for i in y :
            x.append(i)
        nums1 = sorted(x)
        print(nums1)
Solution.merge(Solution, [1,2,3,0,0,0], 3, [2,5,6], 3)