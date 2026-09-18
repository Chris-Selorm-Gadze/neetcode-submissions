class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
   
        '''
        algorithm 
        @use arrays
        @create an arr of 0s for all chars
        loop the len of str(s)
            count ord(s) and increment 1
            count ord(t) and decrement 1 

            if value in count != 0 
                return False 
        return True 
        '''

        if len(s) != len(t):
            return False 

        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False 
        return True 
