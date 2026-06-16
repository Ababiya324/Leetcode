class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        e=[]
        i=0
        s=set()
        p=set()
        n = len(nums)  # Cache length
        if nums.count(0)>=3:
            e.append([0,0,0])
        while i<n:  # Use cached length
            if nums[i] in s:
                i+=1
                continue
            if nums[i]>=0:
                break
            first=nums[i]
            target = -first  # Cache the target (abs of first)
            j=i+1
            k=n-1  # Use cached length
            while j<k:
                current_sum = nums[j]+nums[k]  # Cache the sum
                if current_sum>target:
                    k-=1
                elif current_sum<target:
                    j+=1
                else:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))  # Cache the tuple
                    if triplet not in p:
                        e.append([nums[i], nums[j], nums[k]])
                        p.add(triplet)
                    k-=1
                    j+=1
            s.add(nums[i])
            i+=1
        return e