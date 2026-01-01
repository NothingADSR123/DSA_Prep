class Solution:
    def twoSum(self, nums:list[int], target: int) ->list[int]:
        
#        for i in range(len(nums)):
#            for j in range(i+1,len(nums)):
#                if target-nums[i]==nums[j]:
#                    return [i,j]
        
        d={}
        for i,n in enumerate(nums):
            diff=target-n 
            if diff in d:
                return [d[diff],i]
            d[n]=i
  # Check AGainh
          
# Create an instance of the Solution class
solution = Solution()

# Call the method using the class instance
result = solution.twoSum([2, 3, 5, 7, 8, 9, 5, 7, 5, 4], 7)

# Print the result
print(result)  # Output: [0, 9] or other valid pair indices   
            