class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        position = 0

        for index, value in enumerate(nums):
            if value != 0:
                nums[position], nums[index] = nums[index], nums[position]
                position += 1
        return nums
        