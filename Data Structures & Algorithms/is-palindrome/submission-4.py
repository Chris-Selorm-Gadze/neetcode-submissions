'''
return true if characterws read both sides, ignoring non alphas. 

two-pointer technique. 

                  i j 
 s = "Was it a car or a cat I saw?"
 
 pointer1 = 0 = i
 pointer2 = len(s) - 1 = j

note: if i = j, move both pointers inside. 
      if i = non-alpha and j = non alpha
      move i or j to the next val inwards 

note: if one is one a char and the other on a non-char. main char and move non-char
convert all strings to lowercase. 

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # move left pointer to next letter/number
            while l < r and not s[l].isalnum():
                l += 1

            # move right pointer to previous letter/number
            while r > l and not s[r].isalnum():
                r -= 1

            # compare characters (ignore case)
            if s[l].lower() != s[r].lower():
                return False

            # move both pointers inward
            l += 1
            r -= 1

        return True



















        
                
            