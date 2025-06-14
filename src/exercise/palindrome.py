class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num_str = str(x)

        while len(num_str) > 1:
            if num_str[0] != num_str[-1]:
                return False
            num_str = num_str[1:-1]

        return True

    def isPalindromeWithReverse(self, x: int) -> bool:
        if x < 0:
            return False

        num_str = str(x)[::-1]  # Reverse the string representation of the number
        if num_str == str(x):
            return True

        return False


# from exercise.palindrome import Solution

# solution = Solution()
# print(f"Input: {121}, isPalindrome: {solution.isPalindromeWithReverse(121)}")
# print(f"Input: {-121}, isPalindrome: {solution.isPalindromeWithReverse(-121)}")
# print(f"Input: {10}, isPalindrome: {solution.isPalindromeWithReverse(10)}")
# print(f"Input: {12321}, isPalindrome: {solution.isPalindromeWithReverse(12321)}")
