class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening=[]
        dictionary={'[':']',
        '{':'}','(':')'}
        for i in s:
            if i in dictionary:
                opening.append(i)
            elif len(opening)>0 and i==dictionary.get(opening[-1],''):
                opening.pop()
            else:
                opening.append(i)
        return len(opening)==0
#()[]{}  ])}

