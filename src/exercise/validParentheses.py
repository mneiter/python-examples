class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                return False  # Only parentheses are allowed

        return not stack

# from exercise.validParentheses import Solution

# solution = Solution()
# strs = "()"
# print(f"Input: {strs} Output: {solution.isValid(strs)}")
# strs = "()[]{}"
# print(f"Input: {strs} Output: {solution.isValid(strs)}")
# strs = "(]"
# print(f"Input: {strs} Output: {solution.isValid(strs)}")
# strs = "([)]"
# print(f"Input: {strs} Output: {solution.isValid(strs)}")
# strs = "{[]}"
# print(f"Input: {strs} Output: {solution.isValid(strs)}")
# strs = "{[()]}"
# print(f"Input: {strs} Output: {solution.isValid(strs)}")
# strs = "(("
# print(f"Input: {strs} Output: {solution.isValid(strs)}")
# strs = "("
# print(f"Input: {strs} Output: {solution.isValid(strs)}")
# strs = "))"
# print(f"Input: {strs} Output: {solution.isValid(strs)}")

# class Solution:
#     def isValid(self, strs: str) -> bool:
#         stack = []
#         mapping = {')': '(', '}': '{', ']': '['}

#         for char in strs:
#             if char in mapping.values():
#                 stack.append(char)
#             elif char in mapping:
#                 if not stack or stack.pop() != mapping[char]:
#                     return False
#             else:
#                 # Ignore non-parenthesis characters, or return False if invalid input
#                 return False

#         return not stack

# 20. Valid Parentheses
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.