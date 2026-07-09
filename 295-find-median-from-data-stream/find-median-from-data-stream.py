class MedianFinder:

    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        self.lst.append(num)

    def findMedian(self) -> float:
        self.lst.sort()
        n = len(self.lst)
        if n % 2 == 0:
            return (self.lst[n // 2] + self.lst[n // 2 - 1]) / 2
        else:
            return (self.lst[n // 2])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()