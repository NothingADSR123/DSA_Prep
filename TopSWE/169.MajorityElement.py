# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


#Boyer-Moore
        # count,res=0,0
        # for i in nums:
        #     if count==0:
        #         res=i
        #     if i==res:
        #         count+=1
        #     else:
        #         count+=-1
        # return res
        
# GAand Approach
#         d={}
#         for i in range(len(nums)):
#             if nums[i] in d:
#                 d[nums[i]]+=1
#             else:
#                 d[nums[i]]=1
#         print(d)
#         for i in d:
#             if d[i]==max(d.values()):
#                 maxi=i
#         return (maxi)  


# Brute Force - USing Hash MAP
# def majorityElement(nums):
#     counts = {}
#     for num in nums:
#         counts[num] = counts.get(num, 0) + 1
#         if counts[num] > len(nums) // 2:
#             return num

