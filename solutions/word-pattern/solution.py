class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        s=s.split()
        if len(list(pattern)) != len(s):
            return False
        if len(set(list(pattern))) != len(set(s)):
            return False
        c={}

        for i in range(len(pattern)):
            c[pattern[i]]=c.get(pattern[i],set())|{s[i]}
        for i in c.values():
            if len(i)>1:
             return False
        return True
    