class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freqList = []
        for num, freq in count.items():
            freqList.append([freq, num])
        freqList.sort()

        res = []
        while k != 0:
            res.append(freqList.pop()[1])
            k -= 1
        return res