class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) >= len(num2):
            a, b = num1, num2
        else:
            a, b = num2, num1

        b = '0' * (len(a) - len(b)) + b
        
        d = ''
        r = 0
        
        for i in range(len(a) - 1, -1, -1):
            digit_sum = (ord(a[i]) - ord('0')) + (ord(b[i]) - ord('0')) + r
            d = chr(digit_sum % 10 + ord('0')) + d
            r = digit_sum // 10
        
        if r > 0:
            d = chr(r + ord('0')) + d
        
        return d


        