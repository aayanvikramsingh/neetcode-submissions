class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                tmp = min(heights[i], heights[j]) * (j - i)
                if tmp > max_val:
                    max_val = tmp
        return max_val
