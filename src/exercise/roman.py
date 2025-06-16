from typing import List, Dict

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int: Dict[str, int] = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        roman_before_to_int: Dict[str, int] = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        total: int = 0
        prev_value: int = 0

        list_of_chars: List[str] = list(s)

        while list_of_chars:
            if ''.join(list_of_chars[0:2]) in roman_before_to_int:
                value = roman_before_to_int[''.join(list_of_chars[0:2])]
                total += value
                list_of_chars = list_of_chars[2:]
            else:
                value = roman_to_int[list_of_chars[0]]
                total += value
                list_of_chars = list_of_chars[1:]

        return total

    def romanToInt2(self, s: str) -> int:
        # Map Roman numerals to integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # Result value
        n = len(s)

        for i in range(n):
            current_value = roman_map[s[i]]

            # If this is not the last character and the next character is larger
            # then this is a subtractive pair (like IV or IX)
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= current_value
            else:
                total += current_value

        return total

# from exercise.roman import Solution

# # Example usage:
# input = "III"
# solution = Solution()
# result = solution.romanToInt(input)
# print(f"Input: {input}, Output: {result}") # Output: 3
# input = "LVIII"
# result = solution.romanToInt(input)
# print(f"Input: {input}, Output: {result}") # Output: 58
# input = "MCMXCIV"
# result = solution.romanToInt(input)
# print(f"Input: {input}, Output: {result}") # Output: 1994
# input = "MMXXIII"
# result = solution.romanToInt(input)
# print(f"Input: {input}, Output: {result}") # Output: 2023

# 13. Roman to Integer
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].