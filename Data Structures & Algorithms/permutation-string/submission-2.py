from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        if k > n:
            return False

        need = Counter(s1)   # char counts of s1
        window = Counter()   # char counts in current window of s2

        l = 0
        for r, ch in enumerate(s2):
            # expand window to the right
            window[ch] += 1

            # if window is too big, shrink from the left
            if r - l + 1 > k:
                left_char = s2[l]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                l += 1

            # when window size is exactly k, check permutation
            if r - l + 1 == k:
                if window == need:
                    return True

        return False
