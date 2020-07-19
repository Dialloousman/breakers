def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #handle edgcase --> not passed array with values or array val 1
        if len(nums) is 0 or len(nums) is 1: return []
        
        
        #declare  a dictionary
        numbersMap = {}
        
        #loop through list 
        i = 0
        while i < len(nums):
            key = target - nums[i]
            
            if key in numbersMap: return [numbersMap[key], i]
            
            numbersMap[nums[i]] = i

            i+=1
            
        # return MT array 
        return []


print(twoSum( [2,7,14,15], 9))
