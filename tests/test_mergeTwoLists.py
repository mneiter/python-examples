import unittest
from src.exercise.mergeTwoLists import Solution, ListNode

def list_to_linkedlist(lst: list[int]) -> 'ListNode | None':
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(node: 'ListNode | None') -> list[int]:
    result: list[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_both_empty(self):
        self.assertIsNone(self.solution.mergeTwoLists(None, None))

    def test_one_empty(self):
        l1 = list_to_linkedlist([])
        l2 = list_to_linkedlist([0])
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(linkedlist_to_list(merged), [0])

    def test_example(self):
        l1 = list_to_linkedlist([1,2,4])
        l2 = list_to_linkedlist([1,3,4])
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(linkedlist_to_list(merged), [1,1,2,3,4,4])

    def test_no_overlap(self):
        l1 = list_to_linkedlist([1,2,3])
        l2 = list_to_linkedlist([4,5,6])
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(linkedlist_to_list(merged), [1,2,3,4,5,6])

    def test_all_elements_equal(self):
        l1 = list_to_linkedlist([2,2,2])
        l2 = list_to_linkedlist([2,2])
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(linkedlist_to_list(merged), [2,2,2,2,2])

    def test_negative_values(self):
        l1 = list_to_linkedlist([-10, -5, 0])
        l2 = list_to_linkedlist([-6, -3, 2])
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(linkedlist_to_list(merged), [-10, -6, -5, -3, 0, 2])

    def test_single_element_lists(self):
        l1 = list_to_linkedlist([1])
        l2 = list_to_linkedlist([2])
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(linkedlist_to_list(merged), [1,2])

    def test_long_lists(self):
        l1 = list_to_linkedlist(list(range(0, 50, 2)))
        l2 = list_to_linkedlist(list(range(1, 50, 2)))
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(linkedlist_to_list(merged), list(range(50)))

if __name__ == "__main__":
    unittest.main()