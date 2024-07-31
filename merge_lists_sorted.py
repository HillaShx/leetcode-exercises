from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        repr_str = str(self.val)
        if self.next is not None:
            repr_str += f" -> {self.next.__repr__()}"
        return repr_str
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1, pointer2, merged_pointer = list1, list2, ListNode()
        merged_head = merged_pointer
        while pointer1 or pointer2:
            merged_pointer.next = ListNode()
            if not all([pointer1, pointer2]):
                pointer1, pointer2, merged_pointer = handle_one_none(pointer1, pointer2, merged_pointer)
            elif pointer1.val > pointer2.val:
                merged_pointer.next.val=pointer2.val
                pointer2 = pointer2.next
            else:
                merged_pointer.next.val=pointer1.val
                pointer1 = pointer1.next
            merged_pointer = merged_pointer.next
        return merged_head.next

def handle_one_none(l1, l2, merged_pointer):
    if l1 is None:
        merged_pointer.next.val = l2.val
        l2 = l2.next
    else:
        merged_pointer.next.val = l1.val
        l1 = l1.next
    return l1, l2, merged_pointer


input_data = {
    # 1: {
    #     "list1": ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4))),  # 1,2,4
    #     "list2": ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4))),  # 1,3,4
    # },
    # 2: {
    #     "list1": None,  # -
    #     "list2": None,  # -
    # },
    # 3: {
    #     "list1": None,  # -
    #     "list2": ListNode(),  # 0
    # },
    4: {
        "list1": ListNode(val=-9, next=ListNode(val=3)),  # -9,3
        "list2": ListNode(val=5, next=ListNode(val=7)),  # 5,7
    },
}
