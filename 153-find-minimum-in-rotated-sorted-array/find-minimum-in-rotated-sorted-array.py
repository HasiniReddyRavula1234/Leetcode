class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = nums[0]
        for i in range(len(nums)):
            if min_num > nums[i]:
                min_num = nums[i]
        return min_num