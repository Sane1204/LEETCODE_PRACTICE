class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels={"a","e","i","o","u"}
        count =0
        best=0

     
        for i in range(k):
            if s[i] in vowels:
                count+=1
            best= count
        for right in range(k, len(s)):
            leaving = s[right - k]
            entering = s[right]

            if leaving in vowels:
                count-=1
            if entering in vowels:
                count+=1
            if count>best:
                best= count
        return best
        
                    
           
                

