class Solution(object):
    def majorityFrequencyGroup(self, s):
        """
        :type s: str
        :rtype: str
        """
        c={}
        d={}
        for i in s:
            c[i]=c.get(i,0)+1
        for i in c:
             d.setdefault(c[i], set()).add(i)


        curr=0
        b=set()

        for i in d:
            if len(d[i])==curr:
                b=(d[i])
            elif len(d[i])>curr:
                b.clear()
                curr=len(d[i])
                b=d[i]
        return "".join(b)

