class Solution(object):
    def reverseOnlyLetters(self, s):
        left = 0
        right = len(s) - 1
        e = ''
        
        while left < len(s):
            if right >= 0 and s[left].isalpha() and s[right].isalpha():
                e += s[right]
                right -= 1
                left += 1
            elif not s[left].isalpha():
                e += s[left]
                left += 1
            elif right >= 0 and not s[right].isalpha():
                right -= 1
        
        return e