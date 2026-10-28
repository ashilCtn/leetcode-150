class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            ']': '[',
            '}': '{',
            ')': '(',
        }
        stack = []

        for c in s:
            if c not in hashMap:
                stack.append(c)
            else:
                if not stack or hashMap[c] != stack[-1]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0
        