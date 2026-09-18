class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        algorithm
        @use an a hashmap. Store val $ idx on 1st pass  
        num = target - value 
        
        if num in seen
            return num[val], idx 

        update hashmap 
        '''

        seen = {}

        for idx, val in enumerate(nums):
            num = target - val 

            if num in seen:
                return [seen[num], idx]
            seen[val] = idx 
        
        return None 