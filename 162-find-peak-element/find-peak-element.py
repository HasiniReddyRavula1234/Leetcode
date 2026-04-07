class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lar = -1
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                lar = max(lar, i)
        if lar == -1:
            return 0
        return lar