print("Main script executed.")

from exercise.palindrome import Solution

solution = Solution()
print(f"Input: {121}, isPalindrome: {solution.isPalindromeWithReverse(121)}")
print(f"Input: {-121}, isPalindrome: {solution.isPalindromeWithReverse(-121)}")
print(f"Input: {10}, isPalindrome: {solution.isPalindromeWithReverse(10)}")
print(f"Input: {12321}, isPalindrome: {solution.isPalindromeWithReverse(12321)}")

print(f"Input: {121}, isPalindrome: {solution.isPalindrome(121)}")
print(f"Input: {-121}, isPalindrome: {solution.isPalindrome(-121)}")
print(f"Input: {10}, isPalindrome: {solution.isPalindrome(10)}")
print(f"Input: {12321}, isPalindrome: {solution.isPalindrome(12321)}")
