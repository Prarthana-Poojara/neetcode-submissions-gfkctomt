class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        res =[]
        #Three conditions for this prob: 1)only add open paranthesis if open count < n
        #2) only add closed paranthesis if closed count <open count
        #3) valid IIF open == closed ==n

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closedN)
                stack.pop()
            if closedN<openN:
                stack.append(')')
                backtrack(openN, closedN+1)
                stack.pop()
        backtrack(0,0)
        return res

        