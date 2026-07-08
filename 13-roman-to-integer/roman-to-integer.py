class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s)):
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                n -= values[s[i]]
            else:
                n += values[s[i]]
        return n

