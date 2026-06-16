class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        j=0
        i=0
        d=0
        while i < len(g) and j < len(s):
                    if s[j] >= g[i]:
                        d += 1
                        i += 1
                        j += 1
                    else:
                        j += 1

        return d
        



