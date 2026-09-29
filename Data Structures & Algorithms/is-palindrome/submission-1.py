class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = s.lower()
        res= []
    
        for al in s_new:
            if al.isalnum()== True:
                res.append(al)
        strr = "".join(res)
        i,j = 0,len(strr)-1
        while(i<j):
            if strr[i]==strr[j]:
                i+=1
                j-=1
            else:
                return False
        return True