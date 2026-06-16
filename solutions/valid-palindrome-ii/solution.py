class Solution(object):
    def validPalindrome(self, s):
        if(s==s[::-1]):
            return True
        i=0
        j=len(s)-1
        while(i<j):
            if(s[i]==s[j]):
                i=i+1
                j=j-1
            else:
                newl=s[i+1:j+1]
                newr=s[i:j]
                return newl==newl[::-1] or newr==newr[::-1]
