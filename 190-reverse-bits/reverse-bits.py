class Solution:
    def reverseBits(self, n: int) -> int:
        original = n
        s1 = []
        rev = 0
        for _ in range(32):
            r = original % 2
            s1.append(r)
            original //= 2
        k, s = 0, 0
        for i in s1:
            s = s * 2 + i
        return s