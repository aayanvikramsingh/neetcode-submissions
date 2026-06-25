class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float("inf")
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum >= target:
                    minlen = min(minlen, j - i + 1)
                    break
        if minlen == float("inf"):
            return 0
        return minlen
