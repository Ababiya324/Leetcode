# Documentation: Letter Combinations (Mathematical Approach)

## 1. Core Concept
The solution treats the problem like a fixed grid where each row represents a final combination string, and each column corresponds to a digit in the input.

*   **Total Combinations:** The product of the number of letters mapped to each digit (determines total rows).
*   **Group Size:** The consecutive block size of a single letter. For a given row $j$, the exact letter index is found using:

$$\text{letter\_index} = (j \mathbin{/\!/} \text{group\_size}) \bmod \text{len}(\text{letters})$$

---

## 2. Walkthrough Example: "23"

*   **Total Combinations:** $3 \times 3 = 9$ rows.
*   **Initial State:** `e = ['', '', '', '', '', '', '', '', '']`

### Step 1: Digit '2' ("abc")
*   $\text{group\_size} = 9 \mathbin{/\!/} 3 = 3$ (letters repeat 3 times consecutively).
*   **State:** `e = ['a','a','a', 'b','b','b', 'c','c','c']`

### Step 2: Digit '3' ("def")
*   $\text{group\_size} = 3 \mathbin{/\!/} 3 = 1$ (letters change every row).
*   **State:** `e = ['ad','ae','af', 'bd','be','bf', 'cd','ce','cf']`

---

## 3. Complexity Analysis

*   **Time Complexity:** $\mathcal{O}(4^N \times N)$
*   **Space Complexity:** $\mathcal{O}(4^N)$ (Iterative approach requires no recursion stack; space is utilized solely for storing the output array).
