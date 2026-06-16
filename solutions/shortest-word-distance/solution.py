class Solution(object):
    def shortestDistance(self, wordDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a=0
        b=len(wordDict)
        c=0
        e=set()
        for i in range(len(wordDict)):
            a+=c
            if wordDict[i]==word1:
                e.add(word1)
                if c==0:
                    c=1
                elif a<b and len(e)==2:
                    b=a
                    a=0
                    e=set()
                    e.add(word1)
                a=0
            elif wordDict[i]==word2:
                e.add(word2)
                if c==0:
                    c=1
                elif a<b and len(e)==2:
                    b=a
                    a=0
                    e=set()
                    e.add(word2)
                a=0

        return b



        