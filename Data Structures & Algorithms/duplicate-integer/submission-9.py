'''
return true if there is a duplicate 


              i
    [1, 2, 3, 3] 

no_duplicate = set() -> empty -> 1 -> 2 -> 3 - > False 

note : if i in set : return true : else add i to set 
if traverse with duplcate : return False


'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set() # {1, 2, 3}

        for n in nums: # 3
            if n in nums_set:
                return True

            nums_set.add(n)

        return False 















