class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounts = defaultdict(int)
        for char in t:
            tCounts[char] += 1
        need = len(tCounts.keys())

        have = 0
        substring = ""
        window = defaultdict(int)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in tCounts and window[s[r]] == tCounts[s[r]]:
                have += 1
            
            while have == need:
                length = r - l + 1
                if length < len(substring) or substring == "":
                    substring = s[l : r + 1]

                window[s[l]] -= 1
                if s[l] in tCounts and window[s[l]] < tCounts[s[l]]:
                    have -= 1
                l += 1

        return substring