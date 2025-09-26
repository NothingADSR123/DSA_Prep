# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

def canJump(self, nums: list[int]) -> bool:
#         Bringing Goal (last element) to the starting point
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i +nums[i]>= goal:
                goal = i
        return True if goal==0 else False
        
#         Going to the last element
        # far=0
        # for i in range(len(nums)):
        #     if i>far:
        #         return False
        #     far=max(far,i+nums[i])
        # return True if far>=len(nums)-1 else False