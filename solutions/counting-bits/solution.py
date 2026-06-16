class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        d = [0] * (n + 1)
        for i in range(1, n + 1):
            d[i] = d[i // 2] + (i % 2)
        return d

        