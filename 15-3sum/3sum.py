class Solution:
    ##swapnil
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        i = 0
        n=len(nums)
        nums.sort()
        ans=[]
        while (i<n):
            
            if (i==0 or (i - 1 >= 0  and nums[i] != nums[i-1])):
                firstelement=nums[i]
                target = 0- firstelement 
                pairs = self.twosum(nums, i+1, n-1, target)
                for pair in pairs:
                    triplet =[firstelement, pair[0],pair[1]]
                    ans.append(triplet)
            i+=1
        return ans
            

        
        
    def twosum(self, nums, start, end,target):
            f = start
            s = end 
            pairs=[]
            while(f<s):
                if (f - 1>=start and nums[f-1]== nums[f]):
                    f=f+1
                    continue
                if (s+1 <= end and nums[s+1]==nums[s]):
                    s=s-1
                    continue
                if (nums[f] + nums[s]< target):
                    f+=1
                elif(nums[f] + nums[s] > target):
                    s-=1
                else:
                    pair = [nums[f],nums[s]]
                    pairs.append(pair)
                    f+=1
            return pairs


        