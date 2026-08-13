class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        left =0
        right = len(nums)-1
        n= len(nums)

        while left <= right:
            mid = (left + right)//2

            if nums[0]> nums[mid]:
                ans = nums[mid]
                right = mid -1
            else:
                left = mid+1
        return ans
        