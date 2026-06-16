class Solution(object):
    def lateFee(self, daysLate):
        """
        :type daysLate: List[int]
        :rtype: int
        """
        c=0
        for i in daysLate:
            if i==1:
                c+=1
            elif 2<=i<=5:
                c+=(2*i)
            else:
                c+=(3*i)
        return c
