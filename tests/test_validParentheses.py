import unittest
from src.exercise.validParentheses import Solution

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))

    def test_single_pair(self):
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("[]"))
        self.assertTrue(self.solution.isValid("{}"))

    def test_multiple_pairs(self):
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("{[()]}"))
        self.assertTrue(self.solution.isValid("([])"))
        self.assertTrue(self.solution.isValid("{{[[(())]]}}"))

    def test_incorrect_order(self):
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))
        self.assertFalse(self.solution.isValid("{[}]"))
        self.assertFalse(self.solution.isValid("[(])"))

    def test_unmatched_open(self):
        self.assertFalse(self.solution.isValid("("))
        self.assertFalse(self.solution.isValid("["))
        self.assertFalse(self.solution.isValid("{"))
        self.assertFalse(self.solution.isValid("((("))

    def test_unmatched_close(self):
        self.assertFalse(self.solution.isValid(")"))
        self.assertFalse(self.solution.isValid("]"))
        self.assertFalse(self.solution.isValid("}"))
        self.assertFalse(self.solution.isValid(")))"))

    def test_mixed_valid_invalid(self):
        self.assertFalse(self.solution.isValid("([)"))
        self.assertFalse(self.solution.isValid("({[)]}"))
        self.assertTrue(self.solution.isValid("(([]){})"))

    def test_long_valid(self):
        s = "({[]})" * 1000
        self.assertTrue(self.solution.isValid(s))

    def test_long_invalid(self):
        s = "({[]})" * 999 + "("
        self.assertFalse(self.solution.isValid(s))

    def test_invalid_characters(self):
        self.assertFalse(self.solution.isValid("a"))
        self.assertFalse(self.solution.isValid("1"))
        self.assertFalse(self.solution.isValid("()a"))
        self.assertFalse(self.solution.isValid("([x])"))

if __name__ == "__main__":
    unittest.main()