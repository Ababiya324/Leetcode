class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        j=0
        i=0
        p=len(t)
        q=len(s)
        while i<p and j<q:
            if t[i]==s[j]:
                j+=1
            i+=1
        return j==len(s)

        