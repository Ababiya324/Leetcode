# Letter Combinations of a Phone Number: Iterative (Grid) Approach

## 1. Core Concept

The output is treated as a fixed grid: each **row** is one final combination string, and each **column** corresponds to one input digit. Because the number of rows is known in advance, the result array can be pre-allocated and filled column by column, rather than built up recursively.

- **Total combinations (rows):** the product of the letter-count of each digit. For input `"23"`, this is $3 \times 3 = 9$.
- **Group size:** for a given digit (column), the length of the consecutive block of rows over which a single letter stays fixed before advancing to the next letter.

For a row index $j$, the letter chosen for a given digit is:

$$\text{letter index} = \left\lfloor \frac{j}{\text{group size}} \right\rfloor \bmod \text{len(letters)}$$

The mechanic that makes this work is how `group_size` is obtained. It is **not** recomputed from the total each time. It starts at the total number of combinations and is divided by each digit's letter-count in turn:

```text
group_size = total_combinations
for each digit d (left to right):
    group_size = group_size // len(letters(d))
    for each row j in 0 .. total_combinations - 1:
        letter_index = (j // group_size) % len(letters(d))
        result[j] += letters(d)[letter_index]
```

Because `group_size` is a running quotient, the `"23"` walkthrough below shows `9 // 3` for the first digit but `3 // 3` for the second.

---

## 2. Walkthrough Example: "23"

- **Total combinations:** $3 \times 3 = 9$ rows.
- **Initial state:** `result = ['', '', '', '', '', '', '', '', '']`

### Step 1: Digit '2' → "abc"
- `group_size = 9 // 3 = 3` (each letter occupies a block of 3 consecutive rows).
- **State:** `['a','a','a', 'b','b','b', 'c','c','c']`

### Step 2: Digit '3' → "def"
- `group_size = 3 // 3 = 1` (the letter advances on every row).
- **State:** `['ad','ae','af', 'bd','be','bf', 'cd','ce','cf']`

---

## 3. Complexity Analysis

Let $N$ be the number of input digits. Each digit maps to at most 4 letters (digits 7 and 9), so the number of combinations is bounded by $4^N$.

- **Time:** $\mathcal{O}(4^N \times N)$. There are up to $4^N$ rows, and each row accumulates one character per digit, for $N$ characters total.
- **Space:** $\mathcal{O}(4^N \times N)$. The output holds up to $4^N$ strings, each of length $N$. Auxiliary space beyond the output is $\mathcal{O}(1)$, since the iterative approach maintains no recursion stack.
