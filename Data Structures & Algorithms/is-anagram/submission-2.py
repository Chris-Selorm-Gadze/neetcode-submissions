class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case: if len of string not equal, return false
        # sort the string
        # use two pointer to track chars
        # if not equal,return false

        s_chars = ''.join(sorted(s))
        t_chars = ''.join(sorted(t))

        if len (s) != len(t) :
            return False
         
        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(s_chars) and ptr2 < len(t_chars): 
            if s_chars[ptr1] != t_chars[ptr2]:
                return False

            ptr1 +=1 
            ptr2 += 1 

        return True 