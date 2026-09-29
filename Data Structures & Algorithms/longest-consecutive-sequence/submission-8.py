class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # snums = sorted(nums)
        # count = 1
        # res = 0
        # if not nums:
        #     return 0
        # for i in range(1,len(snums)):
        #     if snums[i]-snums[i-1]==1:
        #         count+=1
        #         res = max(res,count)
        #     elif snums[i]-snums[i-1]==0:
        #         count+=0
        #         res = max(res,count)
        #     else:
        #         count = 1
        # return max(res,count)


        numsset = set(nums)
        temp = True
        res = 0
        count = 1

        if not nums:
            return 0
       
        for num in numsset:
            count =1
            if num - 1 not in numsset:
                temp = True
                while(temp == True):
                    if num+1 in numsset:
                        count+=1
                        res = max(res,count)
                        num=num+1
                    else:
                        temp = False
        return max(res,count)
