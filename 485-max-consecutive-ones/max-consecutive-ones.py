class Solution:
    ##done
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        current = 0
        for i in range(len(nums)):
            if (nums[i] == 0):
                current =0
            else:
                current += 1

            if (current > ans):
                ans=current
        return ans
        

        