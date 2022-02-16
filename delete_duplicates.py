from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"[val={self.val}] -> next={self.next}"


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root_node = head
        curr_node = root_node
        while curr_node and curr_node.next:
            while curr_node.next and curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            curr_node = curr_node.next
        return root_node


input_data = {
    1: {
        "head": ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2)))
    },
    2: {
        "head": ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3, next=ListNode(val=4))))
    },
    3: {
        "head": ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3))))),
    },
    4: {
        "head": ListNode(val=1, next=ListNode(val=1, next=ListNode(val=1)))
    },
    5: {
        "head": None
    }
}
