class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in range(len(s)):
            freq = hashmap.get(s[i], 0) + 1
            hashmap[s[i]] = freq
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1