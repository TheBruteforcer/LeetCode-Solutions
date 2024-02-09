class Solution:
    def majority_element(nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Verify if the candidate is actually the majority element
        count = sum(1 for num in nums if num == candidate)
        if count > len(nums) // 2:
            return candidate
        else:
            return None