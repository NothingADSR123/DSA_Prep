# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
nums1 = [0,0,0,0,0]
m =0
nums2 = [1,2,3,4,5]
n = 5

#BruteForce
for i in range(n):
       nums1[m + i] = nums2[i]
   # Sort nums1
nums1.sort()

#optimal:=>>>
last=m+n-1
i=m-1
j=n-1 
while j>=0:
    if i>=0 and nums1[i]>nums2[j]:
        nums1[last]=nums1[i]
        i-=1
    else:
        nums1[last]=nums2[j]
        j-=1
    last-=1
