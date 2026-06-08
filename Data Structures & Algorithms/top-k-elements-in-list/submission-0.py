class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        topK = []
        for i in range(k):
            maxCount = 0
            for j in count:
                if j in topK:
                    continue
                if count[j] > maxCount:
                    res = j
                    maxCount = count[j]
            topK.append(res)
        return topK
