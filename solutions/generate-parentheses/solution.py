class Solution(object):
    def generateParenthesis(self, n):
        s = {""}
        for _ in range(n):
            d = set()
            for cur in s:
                for k in range(len(cur) + 1):
                    d.add(cur[:k] + "()" + cur[k:])
            s = d
        return list(s)