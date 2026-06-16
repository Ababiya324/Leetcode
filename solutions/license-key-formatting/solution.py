class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        p=[]
        s=s.replace('-','').upper()
        i=len(s)%k
        if i:
         p.append(s[:i])
        for i in range(i,len(s),k):
            p.append(s[i:i+k])
        
        return '-'.join(p)
        
            


        