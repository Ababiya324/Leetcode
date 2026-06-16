class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        temp = []
        for i in licensePlate:
            if i.isalpha():
                temp.append(i.lower())
        
        words.sort(key=len)
        
        for i in words:
            flag = True
            for j in temp:
                if (j not in i) or (temp.count(j)>i.count(j)):
                    flag = False
                    break
            
            if flag:
                return i
            
            
        