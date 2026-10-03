class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res =[ 0 for i in range(len(temperatures))]
        i=0
        for i in range(len(temperatures)):
            while(stack and temperatures[i]>temperatures[stack[-1]]):
                res[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return res
