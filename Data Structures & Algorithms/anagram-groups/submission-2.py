class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramLists = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            lst = anagramLists.get(sortedS, [])
            lst.append(s)
            anagramLists[sortedS] = lst
        
        return list(anagramLists.values())