class Solution:
    from collections import deque 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)): #O(n)
            except_value = nums.pop(i)
            products = math.prod(nums) # O(n) 
            output.append(products)
            nums.insert(i,except_value) # O(n)
        return output