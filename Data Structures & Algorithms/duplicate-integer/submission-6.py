class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDups = set()
        for i in nums:
            if i in noDups:
                return True
            else:
                noDups.add(i)
        return False