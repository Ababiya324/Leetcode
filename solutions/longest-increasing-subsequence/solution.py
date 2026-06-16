class Solution(object):
    def lengthOfLIS(self, nums):
        sub = []  
        for x in nums:
            # Find the index where x should go in sub
            i = bisect.bisect_left(sub, x)

            if i == len(sub):
                # x is larger than everything in sub, extend the list
                sub.append(x)
            else:
                # replace the first element >= x
                sub[i] = x

        return len(sub)
