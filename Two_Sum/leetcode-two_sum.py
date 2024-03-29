class Solution:

    """
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, j in enumerate(nums):
            difference = target - j
            if difference in dict:
                return [dict[difference], i]
            dict[j] = i


    """
Runtime 56ms
Time complexity is O(n) as we iterate through the list once
Look up time for dictionaries is O(1)
    """