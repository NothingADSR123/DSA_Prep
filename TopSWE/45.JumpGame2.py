# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.



# Only OPTIMAL is nice Brute is not applicable 
nums = [2,3,1,1,4]
def jump(self, nums: list[int]) -> int:
    l,r=0,0
    times=0
    while r< len(nums)-1:
        far=0
        for i in range(l,r+1):
            far=max(far,i+nums[i])
        l=r+1
        r=far
        times+=1
    return times