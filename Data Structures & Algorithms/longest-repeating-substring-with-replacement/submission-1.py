class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = collections.defaultdict(int)
        l, longest = 0, 0
        for r in range(len(s)):
            counts[s[r]] += 1

            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r - l + 1))
        
        return longest