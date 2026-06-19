Here is a concise description you can use for your `README.md`:

### Unique Paths (Combinatorics Approach)

Finds the total number of unique paths from the top-left corner to the bottom-right corner of an $m \times n$ grid. Since the robot must make exactly $m - 1$ downward moves and $n - 1$ rightward moves regardless of the path, the problem reduces to calculating the combinations (binomial coefficient) of these moves.

This solution uses `math.factorial` to compute the result directly using the combinations formula:

For any problem it is arrangement of m-1 -> and n-1 ->(downward)

$$\frac{(m + n - 2)!}{(m - 1)! \times (n - 1)!}$$

* **Time Complexity:** $O(m + n)$ to calculate the factorials.
* **Space Complexity:** $O(1)$ auxiliary space.
