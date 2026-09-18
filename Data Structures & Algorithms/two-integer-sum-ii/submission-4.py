'''
return a 1-indexed array which add up to a target 

    p1 = 0
    p2 = 1

     0     1 
    [1,2,3,4] target = 3 

    note: if values at indexes match, append the index to the list 
    return [index - 1]

    curr_sum = ptr1 + ptr2 

    note: while l < r 
          if curr_sum > target: move r inward 
          if curr_sum < target: move l forward  
          if curr_sum == target: return [l +1, r + 1]
          if not pair matches: return an empty list  

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0 , len(numbers) - 1 

        while l < r: 
            curr_sum = numbers[l] + numbers[r]

            if curr_sum > target:
                r -= 1 
            
            elif curr_sum < target:
                l += 1 
            
            else:
                return [l + 1, r + 1]

        return []
















