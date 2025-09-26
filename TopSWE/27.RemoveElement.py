# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
#         k = len(nums)
#         i=0
#         while i<k:
#             if nums[i]==val:
#                 nums[i]=nums[k-1]
#                 k-=1
#             else:
#                 i+=1

#         nums=nums[:k]
#         return k

k=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[k]=nums[i]
        k+=1
# return k