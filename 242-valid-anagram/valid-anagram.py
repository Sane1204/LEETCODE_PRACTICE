class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter={}
        
        if len(s)!= len(t):
            return False
        else:
            for ch in s:
                if ch in letter:
                    letter[ch]+=1
                else:
                    letter[ch]=1
            for ch in t:
                if ch in letter:
                    letter[ch]-=1
                    if letter[ch]<0:
                        return False 
                else:
                   return False 
            else:
                return True
