import math
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class doublyLinkedList:
    def __init__(self):
        self.head = Node("X")
        self.tail = Node("X")
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def pushRight(self, node):
        node.next = self.tail 
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        
    
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        return node

class RandomizedSet:
    
    """
    
    insert value into set -- > return true
    getRandom --> return random val
    remove, val ---> removes val from set -- return true
    if val present in set -- return false
    
    *if len of set is one always return 
    
    
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomSet = {}
        self.setList = doublyLinkedList()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.randomSet:
            return False
        
        node = Node(val)
        self.randomSet[val] = node
        self.setList.pushRight(node)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.randomSet:
            return False
        
        self.setList.removeNode(self.randomSet[val])
        del self.randomSet[val]
        return True
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.randomSet) == 0:
            return False
        
        return choice(list(self.randomSet.keys()))