class Solution:
    ##submitting previous leetcode
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lol={}
        ans = []
        for i in range(len(nums)):
            key = target - nums[i]
            if key in lol:
                ans= [lol[key], i]
                break

            lol[nums[i]] =i
        return ans

        