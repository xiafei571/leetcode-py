# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            second = curr.next
            nextPair = curr.next.next

            # reverse
            curr.next = nextPair
            second.next = curr
            prev.next = second

            # update
            prev = curr
            curr = nextPair

        return  dummy.next
