class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        for i in count:
            if count[i]>len(nums)//2:
                return i
        