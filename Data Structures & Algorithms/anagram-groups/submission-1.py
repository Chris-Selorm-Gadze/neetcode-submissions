class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return a list of anagrams
        # find anagrams and group them
        
        #edge cases: if not list or only one element, return empty / element 
        #check if they are anagrams
        #group it 

        from collections import defaultdict

        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26 

            for char in word:
                count[ord(char) - ord('a')] += 1

            anagrams[tuple(count)].append(word)

        return list(anagrams.values())