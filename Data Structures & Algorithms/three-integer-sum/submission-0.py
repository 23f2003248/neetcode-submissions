class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numss = sorted(nums)
        res = []
        for x in range(len(numss)):
            if x>0:
                if numss[x]==numss[x-1]:
                    continue
            k = 0-numss[x]
            i = x+1
            j = len(numss)-1
            while i<j :
                if numss[i]+numss[j] < k:
                    i+=1
                elif numss[i]+numss[j] > k:
                    j-=1
                else:
                    res.append([numss[i],numss[j],numss[x]])
                    while i<j and numss[i]==numss[i+1]:
                        i+=1
                    while i<j and numss[j]==numss[j-1]:
                        j-=1
                    i+=1
                    j-=1
        return res