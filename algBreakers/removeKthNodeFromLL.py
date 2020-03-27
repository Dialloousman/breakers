# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# !! attemp 2
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Solution: we place fast pointer at n+1 location in the linked List. Then we traverse the linked list until the fast pointer hits null all the while keeping a slow pointer moving from the head. At the end of the traversal we should have the node to remove. We also keep access to the previous node and when we reach the node to remove connect the previous node and the currents next node and point the current node to null. Catches cases: if n is larger than the linked list our inital fast pointer placement will return -1 or falsey. Catch case 2: if we are passed nothing we return -1 or falsey.
        
        # handle catch case for null hed
        if head is None:
            return 
        
        # we place fast pointer if null we return falsey
        fast = head
        i = 1
        
        while i <=  n+1:
            if fast is None:
                return 
            fast = fast.next
            i+=1
        
        # travese linked list keeping prev pointer until !fast
         # when fast is null we simply remove the node by connect and disconnection node accordingly
        prev = head
        curr = head.next
        while fast is not None:
            prev = prev.next
            curr = curr.next
            fast = fast.next
        
        nodeToRemove = curr
        
        prev.next = nodeToRemove.next
        nodeToRemove.next = None
        
        return head  

# failed atttemp two because my test case  ((1) -> (2), 2) returned [] instead of (2)
# why did you struggle:
# Solution: 