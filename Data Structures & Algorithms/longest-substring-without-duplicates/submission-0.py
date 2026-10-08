class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res =[]
        maxlen = 0
        for char in s:
            if char in res:
                ind = res.index(char)
                res = res[ind+1:]
                res.append(char)
                maxlen = max(len(res),maxlen)
            else:
                res.append(char)
                maxlen = max(len(res),maxlen)
        return maxlen