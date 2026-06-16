import math
class Solution(object):
    def arrangeCoins(self, k):
        """
        :type n: int
        :rtype: int
        """
        
        return int((-1 + math.sqrt(1 + 8*k)) / 2)
        