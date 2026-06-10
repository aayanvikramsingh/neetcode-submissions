class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, cnt_z = 1, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt_z += 1
                continue
            prod = prod * nums[i]

        res = [0] * len(nums)

        if cnt_z == 0:
            for i in range(len(nums)):
                res[i] = prod // nums[i]
            return res
        if cnt_z == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = prod
                continue
            return res
        if cnt_z > 1:
            return res
