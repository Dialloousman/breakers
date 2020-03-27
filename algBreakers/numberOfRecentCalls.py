# Attempt: 2
# Failed
# We need to implement a queue in order to solve this, but the problem does NOT make sense to me

# Solution below:
class RecentCounter:
    def __init__(self):
        self.p = collections.deque()   
        
    def ping(self, t: int) -> int:
        self.p.append(t)
        
        while self.p[0] < (t - 3000):
            self.p.popleft()
        
        return len(self.p)

# Solution explanation: We use a queue --> append t --> while --> I HAVE NO IDEAAAAAAAAAAA