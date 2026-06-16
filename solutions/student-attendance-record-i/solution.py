class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if 'LLL' in s:
            return False
        d=0
        for i in s:
            if i=='A':
                d+=1
        return d<2
