class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        a = 1
        for i in (nums):
            if i == a:
                a += 1
        return a