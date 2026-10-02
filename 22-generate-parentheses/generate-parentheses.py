class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1: return ["()"]

        n -= 1
        res = []

        def dfs(O, C, s):
            if not O and not C:
                res.append(s + ")")
                return

            if O > 0:
                dfs(O - 1, C, s + "(")

            if C >= O:
                dfs(O, C - 1, s + ")")

        dfs(n, n, "(")

        return res