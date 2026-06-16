class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        e={'a','e','i','o','u'}
        d=[]
        for i in s:
            if i not in e:
                d.append(i)
        a= "".join(d)
        return a


        