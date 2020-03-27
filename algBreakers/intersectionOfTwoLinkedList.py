# Attempt: 4
# Failed
# Explanation: Used pointers to travese both list -> when either pointer hits hend we set pointer the oppostite list head -> This cancels node differences -> check for equality
# How long to solve: 25

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if headA is None or headB is None: return None
        
        currA = headA
        currB = headB
        
        listAFlag, listBFlag = False, False
        
        while currA and currB: 
            if currA.next is None: 
                currA = headB
                if listAFlag == True: break
                listAFlag = True
            
            if currB.next is None: 
                currB = headA
                if listBFlag == True: break
                listBflag = True
                
            if currA == currB: return currA
                
            currA = currA.next
            currB = currB.next
        
        return None

# Attempt: 3
# Passed
# Explanation: Find the longer list -> Travel the distance of (longer list - shorter list) and place longer list pointer -> Then travel and check for equality

# How long to solve: 30

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None: return None
        
        lenOfA = 0
        lenOfB = 0
        
        currA = headA
        while currA:
            currA = currA.next
            lenOfA+=1
            
        currB = headB
        while currB:
            currB = currB.next
            lenOfB+=1
            
        if lenOfA > lenOfB:
            longerList = headA
            shorterList = headB
            lenToTraverse = lenOfA - lenOfB
        else:
            longerList = headB
            shorterList = headA
            lenToTraverse = lenOfB - lenOfA
            
        i = 0
        while i < lenToTraverse:
            longerList = longerList.next
            i+=1
        
        while longerList and shorterList:
            if longerList == shorterList:
                return shorterList
            
            longerList = longerList.next
            shorterList = shorterList.next
        
        return None

# Attempt: 2
# Passed
# Explanation:
# How long to solve:

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # calculate the difference between the nodes
        listOneCount = 0
        listTwoCount = 0
        currListOne = headA
        currListTwo = headB
        
        while currListOne:
            listOneCount+=1
            currListOne = currListOne.next
            
        while currListTwo:
            listTwoCount+=1
            currListTwo = currListTwo.next
            
        nodeDifferenceNumber = abs(listOneCount - listTwoCount)
            
        # reset head nodes 
        currListOne = headA
        currListTwo = headB

        # move calculated amount in longer list 
        if listOneCount > listTwoCount:
            while nodeDifferenceNumber > 0:
                currListOne = currListOne.next
                nodeDifferenceNumber-=1
        else: 
            while nodeDifferenceNumber > 0:
                currListTwo = currListTwo.next
                nodeDifferenceNumber-=1
        
        # move nodes one by one to see if there is a match
        while currListOne and currListTwo:
            if currListOne == currListTwo:
                return currListOne
            currListOne = currListOne.next
            currListTwo = currListTwo.next
        
        return None