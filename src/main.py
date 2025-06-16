print("Main script executed.")

from exercise.roman import Solution

# Example usage:
input = "III"
solution = Solution()
result = solution.romanToInt(input)
print(f"Input: {input}, Output: {result}") # Output: 3
input = "LVIII"
result = solution.romanToInt(input)
print(f"Input: {input}, Output: {result}") # Output: 58
input = "MCMXCIV"
result = solution.romanToInt(input)
print(f"Input: {input}, Output: {result}") # Output: 1994
input = "MMXXIII"
result = solution.romanToInt(input)
print(f"Input: {input}, Output: {result}") # Output: 2023