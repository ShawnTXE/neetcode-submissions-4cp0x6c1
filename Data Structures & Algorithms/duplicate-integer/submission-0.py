class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set()
        for num in nums:
            if num not in duplicateSet:
                duplicateSet.add(num)
            else:
                return True

        return False