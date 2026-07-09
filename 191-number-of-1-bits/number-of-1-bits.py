class Solution:
    def hammingWeight(self, n: int) -> int:
        rem, count = 0, 0
        while n > 0:
            r = n % 2
            if r == 1:
                count += 1
            rem = rem * 10 + r
            n = n // 2
        return count