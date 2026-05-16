class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = collections.defaultdict(int), collections.defaultdict(int)
        for char in s:
            countS[char] += 1
        
        for char in t:
            countT[char] += 1
        
        return countS == countT