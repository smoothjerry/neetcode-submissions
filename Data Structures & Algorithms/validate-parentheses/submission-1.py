class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        stack = []
        for char in s:
            if char in matches and stack and stack[-1] == matches[char]:
                stack.pop()
            else:
                stack.append(char)

        return False if stack else True