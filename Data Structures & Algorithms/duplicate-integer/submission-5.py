class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        NoDuplicate = set()
        for i in nums:
            if i in NoDuplicate:
                return True
            else:
                NoDuplicate.add(i)
        return False
            