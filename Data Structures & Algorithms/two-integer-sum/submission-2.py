class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      #hashmap ==> key: num and value => index

      valdict = {}
    
      for i , n in enumerate(nums):
        diff = target - n 

        if diff in valdict:
            return [valdict[diff], i]

        valdict[n] = i 
