class Solution(object):
    def backspaceCompare(self, s, t):
        i = len(s) - 1
        j = len(t) - 1
        
        while i >= 0 or j >= 0:
            # Process s to find next valid character
            skip_s = 0
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break
            
            # Process t to find next valid character
            skip_t = 0
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break
            
            # Both have valid characters - compare them
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            # One finished, other didn't
            elif i >= 0 or j >= 0:
                return False
            
            i -= 1
            j -= 1
        
        return True