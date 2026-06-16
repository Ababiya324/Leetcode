class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i=0
        e=len(abbr)
        o=len(word)
        j=0
        p=''
        while i<e:
            if abbr[i].isalpha():
                if  j>=o or abbr[i]!=word[j] :
                    return False
                j+=1
                i+=1
                
            else:
                n=0
                if abbr[i] == '0':            # leading zero not allowed
                    return False
                while i+n<e and abbr[i+n].isdigit():
                    p+=abbr[i+n]
                    n+=1
                j+=int(p)
                i+=n
            n=0
            p=''
            if j>o:
                return False
        return j==o

                    



        