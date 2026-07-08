class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        add=0
        best=0
        
        for i in range(k):
            add+=nums[i]
            best = add
            left = nums[0]

        for i in range(k,len(nums)):
            add+= nums[i] - nums[i-k]
            best = max(best , add)
            
        return best/k
        
        
        
            
                    

        