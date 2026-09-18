class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for idx, val in enumerate(nums):
            num = target - val
            if num in hashmap:
                return [hashmap[num], idx]
            hashmap[val] = idx
        return None