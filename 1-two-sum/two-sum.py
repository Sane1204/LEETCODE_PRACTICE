class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans=[]
        dic={}

        
        for i in range(len(nums)):
            key = target - nums[i]
            if key in dic:
                ans=[dic[key],i]
            else:
                dic[nums[i]]=i
        return ans



        

