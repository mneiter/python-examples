from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the merge process
        dummy = ListNode(0)
        current = dummy
        
        while list1 is not None or list2 is not None:
            if list1 is None:
                current.next = list2
                break
            elif list2 is None:
                current.next = list1
                break

            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        return dummy.next

# from exercise.mergeTwoLists import Solution, ListNode

# def print_list(node: ListNode):
#     while node:
#         print(node.val, end=" -> ")
#         node = node.next
#     print("None")

# solution = Solution()
# list1 = ListNode(1, ListNode(2, ListNode(4)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))
# merged_list = solution.mergeTwoLists(list1, list2)
# print(f"Input: list1 = [1,2,4], list2 = [1,3,4] Output: {print_list(merged_list)}")

# 21. Merge Two Sorted Lists
# Easy
# Topics
# premium lock icon
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.