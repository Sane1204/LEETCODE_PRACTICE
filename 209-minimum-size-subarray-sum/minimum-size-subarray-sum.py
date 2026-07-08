class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        best=float('inf')
        add=0
        for i in range(len(nums)):
            add+=nums[i]
            if target <=add:
                while target<=add:
                    add -= nums[left]
                    best = min(best,i-left+1)
                    left+=1
        if best==float('inf'):
            return 0
        else:
            return best
            