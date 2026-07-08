class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        s1 = (n * (n + 1)) // 2
        
        return s1 - s

























    #    length_array = len(nums)
    #    return (length_array * (length_array+1))//2-sum(nums)