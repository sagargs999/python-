class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if nums.count(num) == 1:
                result.append(num)

        return result
