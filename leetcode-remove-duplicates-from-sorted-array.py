# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
print(Solution.removeDuplicates(Solution, [1,1,2]))