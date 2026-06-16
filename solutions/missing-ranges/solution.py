class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        # c=[]
        # d=[]
        # j=0
        # if nums==[]:
        #     return [[lower,upper]]
        # for i in range(lower,upper+1):
        #     if i not in nums and c==[]:
        #         c.append(i)
        #     if c!=[] and i in nums:
        #         c.append(i-1)
        #         d.append(c)
        #         c=[]
        # if nums and upper>nums[-1]:
        #     d.append([nums[-1]+1,upper])
        # return d
        c=[]
        d=[]
        if len(nums)==0:
            return [[lower,upper]]
        if len(nums)==1:
            if lower<nums[0]:
              c.append([lower,nums[0]-1])
            if upper>nums[0]:
              c.append([nums[0]+1,upper])
            return c
        if upper >nums[-1]:
           nums.append(upper+1)
        i=0
        if lower<nums[0]:
            nums.insert(0,lower)
            c.append([lower,nums[1]-1])
            i=1
        
        while i<len(nums)-1:
            if nums[i]+1 != nums[i+1]:
                c.append([nums[i]+1,nums[i+1]-1])
            i+=1
        return c






            



        