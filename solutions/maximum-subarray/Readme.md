### Maximum Subarray (Kadane's Algorithm)

**Core Idea:**
Iterate through the array while maintaining a running sum of the current subarray. At each element, decide whether to continue the current subarray or reset.

**Key Logic:**

* **Accumulate:** Add the current number to `current_sum`.
* **Track Max:** Update `max_sum` whenever `current_sum` beats the highest sum found so far.
* **Reset on Negative:** If `current_sum` drops below `0`, reset it to `0`. A negative running total will only decrease the sum of any future subarray.

**Complexity:**

* **Time:** $O(n)$ — Single pass through the array.
* **Space:** $O(1)$ — Only tracking two scalar variables.
