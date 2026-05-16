class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # want to replace the characters that are least frequent
        # k is the allowance of different characters in a sliding window of unqiue characters
        longest = 0
        count = defaultdict(int)

        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest