class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = [0] * 26
        for char in range(len(s)):
            char_count[ord(s[char])-ord('a')] += 1
            char_count[ord(t[char])-ord('a')] -= 1

        return all(count==0 for count in char_count)