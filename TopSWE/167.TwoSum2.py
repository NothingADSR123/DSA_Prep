# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if target - numbers[j]==numbers[i]:
        #             return [i+1,j+1]
        left,right=0,len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                return [left+1,right+1]