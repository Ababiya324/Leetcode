class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        o = {}       
        used = set() 
        for i in range(len(s)):
            if s[i] in o:
                if o[s[i]] != t[i]:                      return False
            else:
                if t[i] in used:     
                    return False
                o[s[i]] = t[i]
                used.add(t[i])

        return True




        