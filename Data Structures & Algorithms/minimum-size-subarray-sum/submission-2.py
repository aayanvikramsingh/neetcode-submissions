class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, minlen, sum = 0, float("inf"), 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minlen = min(minlen, r - l + 1)
                sum -= nums[l]
                l += 1

        return 0 if minlen == float("inf") else minlen
