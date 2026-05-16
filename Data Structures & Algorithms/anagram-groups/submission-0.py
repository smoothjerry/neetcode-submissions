class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string make count dict
        # can you make a set of dictionaries?
        countArrToStringList = collections.defaultdict(list)
        for s in strs:
            countS = [0] * 26
            for char in s:
                countS[ord(char) - ord('a')] += 1
            
            countArrToStringList[tuple(countS)].append(s)
        
        res = []
        for anagrams in countArrToStringList.values():
            res.append(anagrams)
        
        return res