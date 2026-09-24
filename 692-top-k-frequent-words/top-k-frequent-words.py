import heapq
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        hashmap = {}
        for i in range(len(words)):
            hashmap[words[i]] = hashmap.get(words[i], 0) + 1
            max_freq = 0
            heap = []
        for word, freq in hashmap.items():
            heapq.heappush(heap, (-freq, word))
        res = []
        for i in range(k):
            freq, word = heapq.heappop(heap)
            res.append(word)
        return res
        
            
        