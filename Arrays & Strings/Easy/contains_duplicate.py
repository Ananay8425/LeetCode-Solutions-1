# Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: # type: ignore
        target = set()
        for num in nums:
            if num in target:
                return True
            target.add(num)
        return False