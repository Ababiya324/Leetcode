class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        a = duration
        for i in range(len(timeSeries)-1):
         x=timeSeries[i+1]-timeSeries[i]
         if x<duration:
            a+=x
         else:
            a+=duration
        return a
        