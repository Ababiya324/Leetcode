class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        dp=[0]*len(sequence)
        
        for i in range(len(sequence)):
            if i<len(word)-1:
                dp[i]=0
            else:
             dp[i]=dp[i-len(word)]*int(word == sequence[i-len(word)+1:i+1]) + int(word == sequence[i-len(word)+1:i+1])
        return max(dp)
        