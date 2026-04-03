class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            if len(nums) == 0:
                return [-1,-1]
            def first():
                i = 0
                j = len(nums) -1
                result = -1
                while(i <= j):
                    mid = (i + j) // 2  
                    if(nums[mid] == target):
                        result = mid
                        j = mid - 1
                    elif(nums[mid] < target):
                        i = mid + 1
                    elif(nums[mid] > target):
                            j = mid - 1
                return result

            def last():
                i = 0
                j = len(nums) -1
                result = -1
                while(i <= j):
                    mid = (i + j) // 2  
                    if(nums[mid] == target):
                        result = mid
                        i = mid + 1
                    elif(nums[mid] < target):
                        i = mid + 1
                    elif(nums[mid] > target):
                            j = mid - 1
                return result
            return [first(), last()]