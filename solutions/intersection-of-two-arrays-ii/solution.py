class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        b={}
        a=set(nums1)
        p=set(nums2)
        d={}
        c=[]
        v=[]
        for i in nums1:
            if i in p:
             b[i]=b.get(i,0)+1
        for j in nums2:
            if j in b and b[j]>0:
                v.append(j)
                b[j]-=1

        return v

        