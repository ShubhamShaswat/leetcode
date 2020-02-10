class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        idx =-1

        for i,item in enumerate(nums):
            if item == target:
                return i

            elif item > target:
                return i


        return i+1
