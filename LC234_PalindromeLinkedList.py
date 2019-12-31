# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        deq = collections.deque()
        while node is not None:
            deq.append(node.val)
            node = node.next
            
            
        while deq:
            if deq[0] == deq[-1]:
                deq.popleft()
                if deq:
                    deq.pop()
                continue
            else:
                return False
            
        return True
