class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(start, remaining, path):

            # found valid combination
            if remaining == 0:
                result.append(path[:])
                return

            # invalid branch
            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                num = candidates[i]

                path.append(num)

                # i not i+1 because we CAN reuse same element
                dfs(i, remaining - num, path)

                path.pop()

        dfs(0, target, [])

        return result

            

