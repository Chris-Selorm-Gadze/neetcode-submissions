class Solution:
    def isValid(self, s: str) -> bool:
        HashMap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for i in s:
            if i not in HashMap:
                stack.append(i)
                continue
            if not stack or stack[-1] != HashMap[i]:
                return False
            stack.pop()

        return not stack
    
    