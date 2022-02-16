from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"[val={self.val}] -> next={self.next}"


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root_res_node = ListNode()
        curr_res_node = root_res_node
        curr_l1 = l1
        curr_l2 = l2
        while (curr_l1 or curr_l2) and curr_res_node:
            if curr_l1 and curr_l2:
                curr_sum = curr_l1.val + curr_l2.val
            elif curr_l1:
                curr_sum = curr_l1.val
            elif curr_l2:
                curr_sum = curr_l2.val
            curr_sum += curr_res_node.val
            if curr_sum > 9:
                curr_sum, curr_res_node = self._handle_tens(curr_sum, curr_res_node)
            curr_res_node.val = curr_sum
            curr_l1 = self._get_next_l_node(curr_l1)
            curr_l2 = self._get_next_l_node(curr_l2)
            next_node = self._get_next_res_node(curr_res_node, curr_l1, curr_l2)
            curr_res_node.next = next_node
            curr_res_node = curr_res_node.next
        return root_res_node

    @staticmethod
    def _handle_tens(curr_sum: int, curr_res_node: Optional[ListNode]):
        curr_sum = curr_sum % 10
        curr_res_node.next = ListNode(val=1)
        return curr_sum, curr_res_node

    @staticmethod
    def _get_next_res_node(curr_res_node: Optional[ListNode], curr_l1: Optional[ListNode], curr_l2: Optional[ListNode]):
        next_node = None
        if curr_res_node.next:
            next_node = curr_res_node.next
        elif (curr_l1 is not None) or (curr_l2 is not None):
            next_node = ListNode()
        return next_node

    @staticmethod
    def _get_next_l_node(l_curr: Optional[ListNode]):
        next_node = None
        if l_curr is not None:
            next_node = l_curr.next
        return next_node


input_data = {
    1: {
        "l1": ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3))),
        "l2": ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    },
    2: {
        "l1": ListNode(),
        "l2": ListNode()
    },
    3: {
        "l1": ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9))))))),
        "l2": ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9)))),
    },
    4: {
        "l1": ListNode(val=2, next=ListNode(val=4, next=ListNode(val=9))),
        "l2": ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=ListNode(val=9)))),
    },
    5: {
        "l1": ListNode(val=8, next=ListNode(val=3, next=ListNode(val=2))),
        "l2": ListNode(val=9, next=ListNode(val=2, next=ListNode(val=1))),
    }
}