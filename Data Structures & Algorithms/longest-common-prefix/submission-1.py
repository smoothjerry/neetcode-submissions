class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[-1])):
            for s in strs:
                if i == len(s) or s[i] != strs[-1][i]:
                    return res
            res += strs[-1][i]
        
        return res