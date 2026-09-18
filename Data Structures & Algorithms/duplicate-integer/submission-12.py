class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        algorithm
        @use a set
        @iterate through the list:
            if value in set:
                return True 
            else 
                return False 
            add value to set
        '''
        
        no_duplicate = set()
        for value in nums:
            if value in no_duplicate:
                return True 
            else:
                no_duplicate.add(value)
        return False
