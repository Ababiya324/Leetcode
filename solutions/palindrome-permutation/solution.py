class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """  
        seen=dict()
        for i in s:
              seen[i]=seen.get(i,0)+1  
        solo = 0
        for value in seen.values():
            if value % 2 == 1:
                solo += 1
            
            if solo > 1:
                return False

        return True