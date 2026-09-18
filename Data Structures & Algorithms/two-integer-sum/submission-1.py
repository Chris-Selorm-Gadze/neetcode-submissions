class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ValueMap = {}
        for i,n in enumerate(nums):
            diff = target - n 
            if diff in ValueMap:
                return [ValueMap[diff],i]
            ValueMap[n] = i