class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lst = []
        for i in range(m):
            lst.append(nums1[i])
        
        for j in range(n):
            lst.append(nums2[j])
        
        lst.sort()
        for i in range(m + n):
            nums1[i] = lst[i]
        