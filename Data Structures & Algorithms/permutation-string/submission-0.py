'''
return a true or false for parameters. 
 fixed_pointer = len(s1)

s1 = "abc", s2 = "lecabee"

note : loop right until its equal lo len of s1
       compare curr window to values in s1
       if valid: return true
       else: move both pointers forward. loop until end of string

'''
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0  
        k = len(s1)
        n = len(s2)
        char_count = Counter(s1)

        if k > n:
            return False

        for r in range(n): # s1 = "abc", s2 = "lecabee"

            while r - l + 1 == k:
                curr_window = s2[l : r + 1]
                if char_count == Counter(curr_window): 
                    return True

                l += 1  

        return False 



        