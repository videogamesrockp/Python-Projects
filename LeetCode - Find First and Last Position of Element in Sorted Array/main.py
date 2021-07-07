class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        for i in range(len(nums)):
            if nums[i]==target:
                num1=i
                break
        for i in range(len(nums)):
            if nums[i]==target:
                num2=i
        return [num1, num2]
