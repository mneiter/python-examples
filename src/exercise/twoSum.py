from typing import List
from abc import ABC, abstractmethod


class TwoSumInterface(ABC):
    @abstractmethod
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass


class Solution(TwoSumInterface):
    def __init__(self):
        print("Solution instance created.")

    def __del__(self):
        print("Solution instance destroyed.")

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []


# from twoSum import Solution

# # Example usage:
# nums = [2, 7, 11, 15]
# target = 9
# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)

# # Another example usage:
# nums2 = [3, 2, 4]
# target2 = 6
# result2 = solution.twoSum(nums2, target2)
# print(result2)

# # Yet another example:
# nums3 = [1, 5, 3, 7]
# target3 = 8
# result3 = solution.twoSum(nums3, target3)
# print(result3)

# 1. Two Sum
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
