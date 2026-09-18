class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a set
        #check if each element in nums is in set
        #if True: return True
        #if not add number to the set
        #return false
        unique_nums = set()
        for i in nums:
            if i in unique_nums:
                return True
            unique_nums.add(i)
        return False
        
        