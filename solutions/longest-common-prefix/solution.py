class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a=''
        
        for j in strs[0]:
            a+=j
            for i in strs:
                if not i.startswith(a):
                    return a[:-1]
        return strs[0]
            