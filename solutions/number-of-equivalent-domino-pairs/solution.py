class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        p=0
        f={}
        for a,b in dominoes:
            key = (min(a, b), max(a, b))
            f[key]=f.get(key,0)+1
        for j in f.values():
                p+=(j*(j-1)//2)
        return p


        