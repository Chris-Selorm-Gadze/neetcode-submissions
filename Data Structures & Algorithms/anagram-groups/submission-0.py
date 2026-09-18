class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagram = defaultdict(list)
        for i in strs:
            sorted_var = ''.join(sorted(i))
            groupAnagram[sorted_var].append(i)
        return groupAnagram.values()
