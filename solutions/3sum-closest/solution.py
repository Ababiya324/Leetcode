class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                curr = nums[i] + nums[left] + nums[right]

                # update closest sum
                if abs(curr - target) < abs(closest - target):
                    closest = curr

                # exact match
                if curr == target:
                    return curr

                # need bigger sum
                elif curr < target:
                    left += 1

                # need smaller sum
                else:
                    right -= 1

        return closest