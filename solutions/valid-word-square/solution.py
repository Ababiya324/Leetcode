class Solution(object):
    def validWordSquare(self, a):
        j = 0
        col = []  # List is faster than string concatenation
        n = len(a)
        
        for i in range(n * n):
            if i % n == 0 and i != 0:  
                if ''.join(col) != a[j]:
                    return False
                col = []
                j += 1
            
            row = i % n
            if j < len(a[row]):
                col.append(a[row][j])
        
        return ''.join(col) == a[j]