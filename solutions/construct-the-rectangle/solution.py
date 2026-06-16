class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(area ** 0.5)   
        while w > 0:
            if area % w == 0:
                l = area // w
                return ([l, w])
                break
            w -= 1
            




        