class Solution(object):
    def numberCount(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        count = 0
        for i in range(a, b + 1):
            if len(set(str(i))) == len(str(i)):
                count += 1
        return count