class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for i in count:
            if count[i] > len(nums) // 2:
                return i
        """

        count = defaultdict(int)
        res = maxCount = 0
        for num in nums:
            count[num] += 1
            if maxCount<count[num]:
                res=num
                maxCount=count[num]
        return res
