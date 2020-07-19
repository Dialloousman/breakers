#https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        sumTable = collections.defaultdict(int)
        sumTable[0] = 1
        currSum = 0
        result = 0
        
        for num in nums:
            
            currSum += num 
            if (currSum - k) in sumTable: 
                result += sumTable[(currSum - k)] 
                
            sumTable[currSum] += 1 
        return result