# Maximum Number of Balloons

## Problem Description

Given a string `text`, return the maximum number of times you can use the characters of `text` to form the word **"balloon"**.

Each character in `text` can only be used once, and you need to have all the required characters to form one complete instance of "balloon".

## Solution Approach

This solution uses a **frequency counting** approach:

1. **Initialize a counter dictionary** for each character in "balloon" (b, a, l, l, o, o, n)
2. **Count occurrences** of each character in the input text
3. **Calculate the limiting factor** by taking the minimum of:
   - Count of 'b' (needed 1 time)
   - Count of 'a' (needed 1 time)
   - Count of 'l' divided by 2 (needed 2 times)
   - Count of 'o' divided by 2 (needed 2 times)
   - Count of 'n' (needed 1 time)

The minimum value represents how many complete "balloon" words can be formed.

## Time & Space Complexity

- **Time Complexity:** O(n) - Single pass through the input text
- **Space Complexity:** O(1) - Fixed-size dictionary with only 7 characters

## Example

```python
text = "loonbalxballpoon"
# b: 2, a: 2, l: 4, o: 4, n: 2
# min(2, 2, 4//2, 4//2, 2) = min(2, 2, 2, 2, 2) = 2
# Output: 2
```

## Code

```python
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counts = {char: 0 for char in 'balloon'}
        for char in text:
            if char in counts:
                counts[char] += 1
        return min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,
            counts['o'] // 2,
            counts['n']
        )
```

## Key Insights

- The word "balloon" contains 7 characters with 'l' and 'o' each appearing twice
- Only characters in "balloon" matter; all others are ignored
- The answer is limited by whichever character has the lowest available count relative to its requirement
