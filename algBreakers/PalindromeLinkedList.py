# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Attempt 3
# Failed
# Attempted most optimal solution but bug in code 
def isPalindrome(self, head: ListNode) -> bool:
        def reverseHalfList(node):
            while node is not None:
                ahead = node.next
                node.next = node
                node = ahead
            return node
        
        if not head:
            return True
        
        if not head.next:
            return True
        
        if not head.next.next:
            if head.val != head.next.val:
                return False
            return True
        
        # find the mid point of the LL using fast and slow and pointer to midpoints next
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # helper function
        backtail = reverseHalfList(slow) 
        # begin to move next pointer to current then return head/curr node
            
        # hold a pointer to our midpoint
        midPoint = slow
        
        curr = head
#        move through both list while list tail pointer is not midpoint
        while (backtail != midPoint):
        # if values are not equal RETURN FALSE
            if backtail.val != head.val:
                return False
        
        # retrun true 
        return True

# Attempt: 2
# Pass
# Not most optimal time space solution
class Solution:
    def xisPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        
        if head.next is None:
            return True
        # find the mid point of list 
        slow = head
        fast = head
        valuesStack = []
        
        while fast and fast.next:
            if fast == None:
                break
            slow = slow.next
            fast = fast.next.next
        
        # push current node value and every other     node value into stack
        
        while slow:
            valuesStack.append(slow.val)
            slow = slow.next
        
        # point curr to beginning of list
        curr = head
        # traverse and pop stack off to check equality
        while len(valuesStack) > 0:
            poppedItem = valuesStack.pop()
            # if any value is not equal return a false
            if curr.val != poppedItem:
                return False
            curr = curr.next
        
        return True