class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a=0
        b=len(height)-1
        res=0
        while a<b:
            res=max(min(height[a],height[b])*(b-a),res)
            if height[a]<height[b]:
                a+=1      
            else:
                b-=1
            
        return res
    
        