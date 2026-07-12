class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lol={}
        


        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in lol:
                    lol[i]+=1
                else:
                    lol[i]=1
            for i in t:
                if i in lol:
                    lol[i]-=1
                    if lol[i] < 0:
                        return False
                else:
                    return False
            return True
            
