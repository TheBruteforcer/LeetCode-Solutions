# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeElement(self, nums : list, val: int) -> int:
        for _ in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
print(Solution.removeElement(Solution, [1,2,1,3,5,6,3,4,6,8,9,6,2,1,11,2,31,1,1,1,1], 1))