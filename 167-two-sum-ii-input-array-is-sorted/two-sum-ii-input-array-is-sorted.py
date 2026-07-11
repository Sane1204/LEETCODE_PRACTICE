class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lol={}
        ans=[]
        for i in range(len(numbers)):
            key = target - numbers[i]
            if key in lol:
                ans=[(lol[key] +1) , (i+1)]
                break 
            
            lol[numbers[i]]= i
        return ans