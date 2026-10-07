class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        lst = []
        for i in range(len(nums)):
            sum += nums[i]
            lst.append(sum)
        return lst