class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        iset = set(nums)
        ans=0

        for num in iset:
            
            if (num-1 not in iset):
                current = num
                count = 1
                while current+1 in iset:
                    count+=1
                    current+=1

                if (count> ans):
                    ans = count 
            
        return ans

            
