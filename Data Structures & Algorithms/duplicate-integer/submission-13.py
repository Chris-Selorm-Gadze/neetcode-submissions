class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        make a set 
        for loop
        if num in set
            return True 
        else:
            add to set 
        '''

        no_dup = set()
        for num in nums:
            if num in no_dup:
                return True 
            else:
                no_dup.add(num)
        
        return False