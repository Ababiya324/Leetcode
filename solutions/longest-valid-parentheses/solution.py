class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]  
        m = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i) 
            else: 
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)  
                else:
                    m = max(m, i - stack[-1])  
        
        return m