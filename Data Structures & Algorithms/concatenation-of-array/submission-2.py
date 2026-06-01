class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #TWO PASS
            ans=[]
            for i in range(2):
                for num in nums:
                    ans.append(num)
            return ans


        