class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        c=0
        minprice=prices[0]
        for i in range(1,len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > c:
                c = prices[i] - minprice
        return c
        