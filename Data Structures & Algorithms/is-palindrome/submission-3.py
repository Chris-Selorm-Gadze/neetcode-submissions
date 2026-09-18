class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        # l and r tracks from front/back
        # if char not alphanumeric, increment/ decrement l/r
        #if l != r, return False
        #return True if none exists

        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1

            while l<r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
               
            l += 1
            r -= 1

        return True 
                
            