class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        length = 1
        max_length = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
        max_length = max(max_length, length)
        return max_length
        