class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counts = defaultdict(int)
        for char in s1:
            s1Counts[char] += 1
        
        windowCounts = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            windowCounts[s2[r]] += 1
            while r - l + 1 > len(s1):
                windowCounts[s2[l]] -= 1
                if windowCounts[s2[l]] == 0:
                    del windowCounts[s2[l]]
                l += 1
            
            if windowCounts == s1Counts:
                return True

        return False