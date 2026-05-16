class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for s in strs:
            charOccurrences = [0] * 26
            for char in s:
                charOccurrences[ord(char) - ord('a')] += 1
            
            counts[tuple(charOccurrences)].append(s)


        return list(counts.values())