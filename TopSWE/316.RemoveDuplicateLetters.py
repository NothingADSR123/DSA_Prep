# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

#         k=0
#         seen= set()
#         for i in range(len(nums)):
#             if nums[i] not in seen :
#                 nums[k]=nums[i]
#                 k+=1
#                 seen.add(nums[i])
#         return k  

     
    #  OPtimal Approach 
            # k=1
            # for i in range(1,len(nums)):
            #     if nums[i]!=nums[i-1]:
            #         nums[k]=nums[i]
            #         k+=1
            # return k