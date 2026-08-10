class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans= []
        right = len(numbers)-1
        left = 0

        for i in range(len(numbers)):
            if numbers[left]+ numbers[right]> target:
                right-=1
            elif numbers[left]+ numbers[right]< target:
                left+=1
            else:
                ans=[left+1,right+1]
        return ans

