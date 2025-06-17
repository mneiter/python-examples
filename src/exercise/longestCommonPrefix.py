from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:        
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# from exercise.longestCommonPrefix import Solution

# solution = Solution()
# strs = ["flower","flow","flight"]
# print(f"Input: {strs} Output: {solution.longestCommonPrefix(strs)}")
# strs = ["dog","racecar","car"]
# print(f"Input: {strs} Output: {solution.longestCommonPrefix(strs)}")
# strs = ["interspecies", "interstellar", "interstate"]
# print(f"Input: {strs} Output: {solution.longestCommonPrefix(strs)}")
# strs = ["throne", "throne"]
# print(f"Input: {strs} Output: {solution.longestCommonPrefix(strs)}")
# strs = ["", "b"]
# print(f"Input: {strs} Output: {solution.longestCommonPrefix(strs)}")
# strs = ["a"]
# print(f"Input: {strs} Output: {solution.longestCommonPrefix(strs)}")
# strs = ["ab", "a"]
# print(f"Input: {strs} Output: {solution.longestCommonPrefix(strs)}")

# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.