class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left =0 
        best=0
        zeroes = 0

        for i in range(len(nums)):
            if nums[i]==0:
                zeroes+=1
        
            while zeroes>k:
                if nums[left]==0:
                    zeroes-=1
                left+=1

            best=max(best,i - left +1 )
        return best


        
