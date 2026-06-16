class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        p={}
        for i in s:
            p[i]=p.get(i,0)+1
        for j in range(len(s)):
            if p[s[j]]==1:
                return j
        return -1

        