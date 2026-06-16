class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:
            return []
        d=[str(nums[0])]
        b=0
        for i in range(len(nums)-1):
            if nums[i]+1!=nums[i+1]:
              if nums[i]!=int(d[b]):
                d[b]+='->'+str(nums[i]) 
                d.append(str(nums[i+1]))
                b+=1
              else:
                d.append(str(nums[i+1]))
                b+=1
        if nums[-1]!=int(d[-1]):
         d[-1]+='->'+str(nums[-1])  
        return d