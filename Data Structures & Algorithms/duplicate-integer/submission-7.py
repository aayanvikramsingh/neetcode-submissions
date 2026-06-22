class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
            if count[nums[i]] > 1:
                return True
        return False
