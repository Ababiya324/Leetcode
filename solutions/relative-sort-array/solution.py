class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        d={}
        f=[]
        e=set(arr2)
        g=[]
        for i in sorted(arr1):
            if i in e:
              d[i]=d.get(i,0)+1
            else:
                g.append(i)

        for i in arr2:
            if i in d:
                while d[i]>0:
                 f.append(i)
                 d[i]-=1
           

        return f+g


        