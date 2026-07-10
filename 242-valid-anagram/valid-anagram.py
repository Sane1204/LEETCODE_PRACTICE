class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter={}
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in letter:
                    letter[i]+=1
                else:
                    letter[i] = 1
            for i in t:
                if i in letter:
                    letter[i] -=1
                    if letter[i]<0:
                        return False
                else:
                    return False
            else:
                return True
                    
                
                
        


