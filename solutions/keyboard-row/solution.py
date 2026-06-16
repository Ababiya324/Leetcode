class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        
        result = []
        for word in words:
            word_lower = set(word.lower())
            for row in rows:
                if word_lower <= row:  
                    result.append(word)
                    break
        
        return result



