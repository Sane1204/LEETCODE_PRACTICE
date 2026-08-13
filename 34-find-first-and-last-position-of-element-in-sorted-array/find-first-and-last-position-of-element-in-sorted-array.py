class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findleft(nums,target)
        right = self.findright(nums,target)

        return ([left,right])
    
    def findleft(self,nums,key):
        left =0
        right= len(nums)-1
        ans=-1

        while left<= right:
            mid = (left +right)//2
            if nums[mid] < key:
                left  = mid +1
            elif nums[mid] > key:
                right = mid -1 
            else:
                ans = mid 
                right = mid -1
        return ans 

    def findright(self,nums,key):
        left =0
        right= len(nums)-1
        ans=-1

        while left<= right:
            mid = (left +right)//2
            if nums[mid] < key:
                left  = mid +1
            elif nums[mid] > key:
                right = mid -1 
            else:
                ans = mid 
                left = mid+1 
        return ans
        