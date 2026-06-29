class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i <= j:
            s = nums[i] + nums[j]
            if s == target:
                return [i + 1, j + 1]
            elif s < target:
                i += 1
            else: 
                j -= 1
















        # i, j, sum = 0, len(nums) - 1, 0
        # while i <= j:
        #     sum = nums[i] + nums[j]
        #     if sum == target:
        #         return [i + 1, j + 1]
        #     elif sum < target:
        #         i += 1
        #     else:
        #         j -= 1