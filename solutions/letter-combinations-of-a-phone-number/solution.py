class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        l=1
        for i in digits:
            l*=len(d[i])
        m=l
        e=['']*l
        for i in digits:
            m/=len(d[i])
            for j in range(l):
                e[j]+=d[i][(j/m)%(len(d[i]))]
        return e
                

