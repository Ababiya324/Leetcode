class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        result = [float('inf')] * n
        
        # First pass: left to right - find distance to nearest 'c' on the LEFT
        prev_c_pos = float('inf')
        for i in range(n):
            if s[i] == c:
                prev_c_pos = i
            if prev_c_pos != float('inf'):
                result[i] = i - prev_c_pos
        
        # Second pass: right to left - find distance to nearest 'c' on the RIGHT
        next_c_pos = float('inf')
        for i in range(n-1, -1, -1):
            if s[i] == c:
                next_c_pos = i
            if next_c_pos != float('inf'):
                result[i] = min(result[i], next_c_pos - i)
        
        return result