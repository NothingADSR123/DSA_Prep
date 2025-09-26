# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

def strStr(haystack: str, needle: str) -> int:
    m, n = len(haystack), len(needle)
    if n == 0:
        return 0  # Empty needle is always found at index 0

    for i in range(m - n + 1):  # Iterate over all possible starting positions
        if haystack[i:i + n] == needle:  # Check if substring matches
            return i

    return -1


# Sab equally efficient hain and this best The question is axtually shit and sol is tricky 