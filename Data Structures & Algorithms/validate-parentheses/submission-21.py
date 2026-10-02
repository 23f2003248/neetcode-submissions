class Solution:
    def isValid(self, s: str) -> bool:
        if s == "[]":
            return True
        store = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        stack = deque()
        for i in range(len(s)):
            if s[i] in store.values():
                stack.append(s[i])
            else:
                if stack:
                    if store[s[i]] != stack.pop():
                        return False
                else:
                    return False
        return not stack