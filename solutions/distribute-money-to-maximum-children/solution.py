class Solution(object):
    def distMoney(self, money, children):
        # Each child needs at least 1 dollar
        if money < children:
            return -1
        
        # If we have more than enough for everyone to get 8
        if money > 8 * children:
            return children - 1  # Can't give more than 8 to all
        
        # Distribute 1 dollar to each child first
        money -= children
        
        # How many can get 7 more dollars (to total 8)?
        count = money // 7
        remainder = money % 7
        
        # Edge case: If last child would get exactly 3 more (4 total)
        if count == children - 1 and remainder == 3:
            return count - 1
        
        return min(count, children)