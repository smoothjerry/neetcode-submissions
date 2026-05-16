class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n sets of open '(' and close ')'
        # return a list of well-formed parens strings using n parens
        # n sets of open and close means I have n '(' to use and n ')' to use
        # ))(( -> invalid
        
        # len of one of the output strings is 2n
        # at pos 0 of the output string, two choices: ( or ) -> only open is valid
        # if # of closes is ever greater than # opens, do not continue down the path

        # Solution
        # we want to build a solution set containing strings of length 2n
        # for position in range(2n) -> branch from this starting point based on what parens we can add here
        # 
        
        solution = set()
        
        def dfs(numOpen, numClose, stringArray):
            if len(stringArray) == 2 * n:
                solution.add(''.join(stringArray))
            
            if numClose > numOpen:
                return
            
            if numOpen < n:
                copy = stringArray.copy()
                copy.append('(')
                dfs(numOpen + 1, numClose, copy)

            if numClose < n:
                copy = stringArray.copy()
                copy.append(')')
                dfs(numOpen, numClose + 1, copy)

    
        dfs(1, 0, ['('])
        return list(solution)