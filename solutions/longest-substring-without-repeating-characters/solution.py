class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=0
        b=""
        i=0
        j=0
        d=[]
        while(i<len(s)):
            if (s[i] not in b):
                b+=s[i]
            elif (s[i]==b[0]):
                b+=s[i]
                b=b[1:]
                d.append(len(b))
            else:
                d.append(len(b))
                b+=s[i]
                b=b[b.find(s[i])+1:]
            i+=1
        d.append(len(b))
        return max(d)
                


            