# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        output=""
        for i in range(len(strs[0])):
            for string in strs:
                if i==len(string) or string[i]!= strs[0][i]:
                    return output
            output+=strs[0][i]
        return output