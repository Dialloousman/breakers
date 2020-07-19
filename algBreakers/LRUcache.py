# Attempt: 7
# SUCCESS!
# Explananation: I was able to implement the doubly linked list. If the key is in the cache simply update the values of the node and insert the updated Node as MOST RECENTLY USED. The put method was most likely what was tripping me up.



#build a queue 

#build a node class
class Node:
  def __init__(self, key, value=None):
    self.key = key
    self.value = value
    self.next = None
    self.prev = None

#build doubly LL
class doublyLinkedList:
  def __init__(self):
    self.head = Node("head")
    self.tail = Node("Tail")
    self.head.next = self.tail
    self.tail.prev = self.head
    
  def pushLeft(self, node):
    tempNext = self.head.next
    self.head.next = node
    node.prev = self.head
    node.next = tempNext
    tempNext.prev = node
    
  
  def popRight(self):
    return self.removeNode(self.tail.prev)
  
  def removeNode(self, node):
    nodeToRemove = node
    node.prev.next = node.next
    node.next.prev = node.prev 
    return nodeToRemove

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.queue = doublyLinkedList()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #if key not in dictionary return -1
        #remove node for LL
        #pushLeft node just removed
        #return value 
        
        if key not in self.cache: return -1
        
        nodeToGet = self.queue.removeNode(self.cache[key])
        self.queue.pushLeft(nodeToGet)
        return nodeToGet.value
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        nodeToAdd = Node(key, value)
        
        if key in self.cache: 
          #update values
          self.cache[key].value = value
          nodeToRemoveAndPushRight = self.queue.removeNode(self.cache[key])
          self.queue.pushLeft(nodeToRemoveAndPushRight)
          return
        
        if len(self.cache) < self.capacity:
          #add to our queueu
          #add to dictionary
          self.queue.pushLeft(nodeToAdd)
          self.cache[key] = nodeToAdd
          return 
        
        #eject the last node in list and remove from dictioanry
        #pushleft new node
        #add new key val pair to dictionary
        del self.cache[self.queue.popRight().key]
        self.queue.pushLeft(nodeToAdd)
        self.cache[key] = nodeToAdd
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Attempt: 3
# Failed
# Explananation: I've made progress in understanding the concept. I implmemented a python deque to act as my queue and used an object to allow me to access my data in constant time.

class LRUCache:

    def __init__(self, capacity: int):
        self.deck = deque()
        self.cache = {}
        self.capacity = capacity
        self.count = 0
        

    def get(self, key: int) -> int:
        if not self.cache[key]: return -1
        
        valueToGet = self.cache[key] 
        self.deck.appendleft(valueToGet) 
        return valueToGet['value']
            

    def put(self, key: int, value: int) -> None:
        if self.count < self.capacity:
            self.deck.appendleft({"key":key, "value":value})
            pairToPutInObject = self.deck[0] 
            self.cache[key] = pairToPutInObject
            self.capacity+=1
        else:
            self.deck.pop()
            self.deck.appendleft({key, value})
            self.deque[0] = pairToPutInObject
            self.cache[key] = pairToPutInObject
            self.capacity+=1
        