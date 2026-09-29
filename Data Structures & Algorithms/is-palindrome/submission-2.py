class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = s.lower()
        res= list(s_new)
        strr = "".join(res)

        i,j = 0,len(strr)-1
        while(i<j):
            if strr[i].isalnum()==False:
                i+=1
            elif strr[j].isalnum()==False:
                j-=1
            elif strr[i]==strr[j] :
                i+=1
                j-=1
            else:
                return False
        return True