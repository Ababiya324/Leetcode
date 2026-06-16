class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left0=0
        left1=1
        while left1<len(nums) and left0<len(nums):
            if nums[left0]%2!=0 and nums[left1]%2!=1:
                nums[left0],nums[left1]=nums[left1],nums[left0]
                left0+=2
                left1+=2
            elif nums[left0]%2==0:
                left0+=2
            elif nums[left1]%2==1:
                left1+=2
        return nums



        