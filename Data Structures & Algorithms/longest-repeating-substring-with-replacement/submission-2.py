class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, l = 0, 0
        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            
            while r - l + 1 - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest

    

