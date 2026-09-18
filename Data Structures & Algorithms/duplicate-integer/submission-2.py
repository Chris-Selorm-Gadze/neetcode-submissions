class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniquevalue = set()
        for i in nums:
            if i in uniquevalue:
                return True
            uniquevalue.add(i)
        return False

# Time complexity 0(n)