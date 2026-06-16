class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        a=[1,1]
        b=self.getRow(rowIndex-1)
        for i in range(len(b)-1):
            a.insert(i+1,b[i]+b[i+1])
        return a
        