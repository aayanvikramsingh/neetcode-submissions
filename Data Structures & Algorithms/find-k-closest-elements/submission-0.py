class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []
        res = []
        for i in range(len(arr)):
            diff.append(abs(arr[i] - x))
        for i in range(k):
            min_diff = float("inf")
            count = 0
            for j in range(len(arr)):
                min_diff = min(min_diff, diff[j])
            count = diff.count(min_diff)
            if count >= 1:
                indexes = [i for i, x in enumerate(diff) if x == min_diff]
                res.append(arr[min(indexes)])
            arr.remove(res[-1])
            diff.remove(diff[min(indexes)])
        return sorted(res)
