class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        d=sorted(intervals)
        for i in range(len(d)-1):
            if d[i][1]>d[i+1][0] or d[i][0]==d[i+1][0]:
                return False
        return True
        