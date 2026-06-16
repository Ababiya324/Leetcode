class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a!=b:
            return len(a) if len(a)>len(b) else len(b)
        else:
            return -1