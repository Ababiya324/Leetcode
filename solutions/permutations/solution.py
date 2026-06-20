class Solution(object):
    def permute(self, nums, arr=None,arr2=None):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if arr is None:
            arr = []
            arr2 = []
            
        if len(nums) == 0:
            arr.append(list(arr2)) 
            return 
            
        for i in range(len(nums)):
            pick = nums[i]
            arr2.append(pick)
            self.permute(nums[:i] + nums[i+1:], arr, arr2)
            arr2.pop()
            
        return arr

        