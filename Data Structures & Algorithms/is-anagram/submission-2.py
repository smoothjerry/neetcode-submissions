class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(word):
            counter = {}
            for char in word:
                counter[char] = 1 + counter.get(char, 0)
            
            return counter

        sCount = count(s)
        tCount = count(t)

        return tCount == sCount

