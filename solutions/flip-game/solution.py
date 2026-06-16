class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """
        if len(currentState)<2 :
            return []
        k=[]
        d=''
        pos=0
        for i in range(len(currentState)-1):
            if currentState[i:i+2]=='++':
                d=currentState[:i]+'--'+currentState[i+2:]
                k.append(d)
        return k
    