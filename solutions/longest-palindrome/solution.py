class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        p=0
        q=0
        a={}
        for i in s:
            a[i]=a.get(i,0)+1
        for i in a:
            if a[i]>=2:
              p+=(a[i]//2)*2
            if a[i]%2==1:
                q=1
        return p+q


        
        