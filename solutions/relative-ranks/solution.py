class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_scores = sorted(score, reverse=True)
    
    # Map score to rank
        rank_map = {}
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        for i in range(len(sorted_scores)):
            if i < 3:
                rank_map[sorted_scores[i]] = medals[i]
            else:
                rank_map[sorted_scores[i]] = str(i + 1)
        
        # Return ranks in original order
        return [rank_map[s] for s in score]

        
            
        