class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        else:
                a=[1,1]
                prev = self.generate(numRows-1)
                for i in range(len(prev[-1])-1):
                    
                    a.insert(i+1,prev[-1][i]+prev[-1][i+1])
                return  prev + [a] 
        