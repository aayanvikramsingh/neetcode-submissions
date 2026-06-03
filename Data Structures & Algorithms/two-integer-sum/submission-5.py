class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i,num in enumerate(nums):
            l.append([num,i])
        l.sort()

        left,right=0,len(nums)-1
        while(left<right):
            cur=l[left][0]+l[right][0]
            if(cur==target):
                return [min(l[left][1],l[right][1]),max(l[left][1],l[right][1])]
            elif cur<target:
                left+=1
            else:
                right-=1
        return []
        
