## LeetCode 46. Permutations

### Problem Description

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

### My Solution: Backtracking (Recursion)

#### The Initial Bug

The initial implementation ran into a `RuntimeError: maximum recursion depth exceeded`. This happened due to two critical bugs in the backtracking logic:

1. **Infinite Loop Slicing:**
The recursive call was passing `nums[:i] + nums[i:]`. Because `nums[i:]` includes the element at index `i`, the element picked was never actually removed from the pool. The length of `nums` never decreased, meaning the base case (`len(nums) == 0`) was never met.
2. **Object Reference Mutation:**
Appending `arr2` directly to the results array via `arr.append(arr2)` passed a reference to the mutable list. When backtracking triggered `.pop()`, it altered the values already saved in the final results.

#### The Fix

* **Correct Slicing:** Modified the recursion step to pass `nums[:i] + nums[i+1:]`, which correctly excludes the currently picked element and shrinks the problem space.
* **Deep Copying Results:** Modified the base case to append a shallow copy of the path: `arr.append(list(arr2))`. This freezes the completed permutation snapshot before backtracking continues.

### Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N \cdot N!)$ where $N$ is the length of `nums`. There are $N!$ unique permutations, and copying each list into the result takes $\mathcal{O}(N)$ time.
* **Space Complexity:** $\mathcal{O}(N!)$ to store all the permutations, alongside an $\mathcal{O}(N)$ recursion call stack depth.
