class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word==word.upper() or word==word.lower() or (word[0].isupper() and word[1:].islower())
        