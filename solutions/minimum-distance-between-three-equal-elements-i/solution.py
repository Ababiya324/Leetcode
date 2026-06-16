class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = pos.get(nums[i], []) + [i]
        min_dist = float('inf')
        for indices in pos.values():
            if len(indices) >= 3:
                n = len(indices)
                for i in range(n):
                    for j in range(i+1, n):
                        for k in range(j+1, n):
                            dist = abs(indices[i]-indices[j]) + abs(indices[j]-indices[k]) + abs(indices[k]-indices[i])
                            if dist < min_dist:
                                min_dist = dist

        return -1 if min_dist == float('inf') else min_dist
