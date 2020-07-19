#https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2==1:
            return False
            
        n = len(nums)
            
        sumPart = sum(nums)//2
        
        def dpRecursion(currSum, i, memo):
            
            memoKey = (currSum, i)
            
            if memoKey in memo:
                return memo[memoKey]
            
            if currSum == sumPart:
                return True
            
            if currSum > sumPart:
                return False
            
            if i >= n:
                return False

            memo[memoKey] = dpRecursion( currSum+nums[i], i+1, memo ) or dpRecursion(currSum, i+1, memo)
            print(list(memo.items()))
            return memo[memoKey]
        
        return dpRecursion(0, 0, {})