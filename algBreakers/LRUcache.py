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
        