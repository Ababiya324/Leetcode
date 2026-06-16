class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)==len(set(nums)):
            return False
        d=set()
        for i in range(len(nums)):
            a=nums[i]
            if a in d:
                    return True
            
            if a not in d:
                d.add(nums[i])
            if len(d)>k:
                d.remove(nums[i-k])
        return False
        