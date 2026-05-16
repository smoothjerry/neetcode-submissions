class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        for char in s:
            sCount[char] = 1 + sCount.get(char, 0)
        
        tCount = {}
        for char in t:
            tCount[char] = 1 + tCount.get(char, 0)

        return tCount == sCount