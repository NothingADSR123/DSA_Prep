# 42. Trapping Rain Water {Hard}
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution:
    def trap(self, height: list[int]) -> int:


#         Brute Force TIme Limit
        # total=0
        # for i in range(len(height)):
        #     leftmax=max(height[:i+1])
        #     rightmax=max(height[i:])
        #     total+=max(0,min(leftmax,rightmax)-height[i])
        # return total
    
    
    
    
    
#     Optimal but using O(n) memory 
#         if len(height)==0:
#             return 0

#         leftmax=[1]*len(height)
#         rightmax=[1]*len(height)
#         total=0

#         leftmax[0]=height[0]
#         for i in range(1,len(height)):
#             leftmax[i]=max(leftmax[i-1],height[i])


#         rightmax[-1]=height[-1]
#         for i in range(len(height)-2,-1,-1):
#             rightmax[i]=max(rightmax[i+1],height[i])

#         for i in range(len(height)):
#             total+=max(0,min(leftmax[i],rightmax[i])-height[i])
#         return total





        # Optimal atmostttt
        if not height:
            return 0

        l,r=0,len(height)-1
        leftmax,rightmax=height[l],height[r]
        total=0

        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                total+=leftmax-height[l]
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                total+=rightmax-height[r]

        return total