# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        for x in nums:
            for _ in range(nums.count(x) - 1):
                nums.remove(x)
        return nums
print(Solution.removeDuplicates(Solution, [1,2,1]))