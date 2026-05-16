class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i, j = 0, 0
        chars = set()
        while i <= j and j < len(s):
            if s[j] not in chars:
                chars.add(s[j])
                j += 1
                longest = max(longest, j - i)
            else:
                chars.remove(s[i])
                i += 1
    
        return longest