class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = False
        nums = sorted(nums)
        for i in range(1, len(nums)):
            j = i - 1
            if nums[i] == nums[j]:
                flag = True
        return flag
