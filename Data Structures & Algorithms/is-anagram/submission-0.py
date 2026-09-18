class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_schar_list =  ''.join(sorted(s))
        sorted_tchar_list =  ''.join(sorted(t)) 
            
        if sorted_schar_list == sorted_tchar_list:
            return True
        else:
            return False