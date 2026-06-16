class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
class Solution(object):
    def findRestaurant(self, list1, list2):
        set2 = set(list2)   # step 1: common check
        d = {}              # restaurant -> index in list1 (only if common)

        for i in range(len(list1)):
            if list1[i] in set2:
                d[list1[i]] = i

        best = float('inf')
        c = []

        for j in range(len(list2)):
            s = list2[j]
            if s in d:  # common
                total = d[s] + j
                if total < best:
                    best = total
                    c = [s]
                elif total == best:
                    c.append(s)

        return c

        