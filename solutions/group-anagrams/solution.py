class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        s = []
        
        for i in strs:
            e = "".join(sorted(i))
            if e not in d:
                d[e] = len(s)
                s.append([])
            s[d[e]].append(i)
            
        return s

        