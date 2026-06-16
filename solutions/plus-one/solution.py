class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits==[9]:
            return [1,0]
        digits[-1]+=1
        for i in range(len(digits)-2,-1,-1):
            digits[i]+=digits[i+1]//10
            digits[i+1]%=10
        if digits[0]==10:
            digits[0]=digits[0]%10
            digits.insert(0,1)
        return digits
        
        