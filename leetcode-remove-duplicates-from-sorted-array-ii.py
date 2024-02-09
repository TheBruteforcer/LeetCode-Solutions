# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self, nums ) -> int:

        index = 1
        occurance = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurance += 1
            else:
                occurance = 1

            if occurance <= 2:
                nums[index] = nums[i]
                index += 1
        
        return index
print(Solution.removeDuplicates(Solution, [1,1,1,2,2,2,3,3,4,4]))