class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=s.split()
        for i in range(len(d)):
            d[i]=d[i][::-1]
        return ' '.join(d)
        