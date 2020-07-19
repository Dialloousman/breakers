#https://leetcode.com/problems/target-sum/
class Solution:
    def DFStargetSumWays(self, nums, amount, S):
        if not nums:
            
            if amount == S:
                return 1
                # self.targetSumsWays += 1
                
            return 
        
        if amount in self.memo:
            return self.memo[amount]
        
        
        numCopy = nums[:]
        poppedNum = numCopy.pop()
        
        amounToAdd = poppedNum
        amounToSub = -(poppedNum)
        
        self.memo[amount] += self.DFStargetSumWays(numCopy, amount+amounToAdd, S)
        self.memo[amount] -= self.DFStargetSumWays(numCopy, amount+amounToSub, S)
        
        