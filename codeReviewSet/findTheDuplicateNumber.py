#https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums):
        
        slow = fast = nums[0]
        
        while True:
            
            slow = nums[slow]

            fast = nums[fast]
            fast = nums[fast]
            
            if slow == fast:
                print(nums[slow])
                break
                
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow