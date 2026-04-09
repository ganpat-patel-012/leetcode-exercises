# 27. Remove Element

**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/remove-element/

## Problem

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place. Return the number of elements in `nums` which are not equal to `val`.

The relative order of remaining elements may be changed. It does not matter what values are left beyond the returned count.

## Example

```
Input:  nums = [3, 2, 2, 3], val = 3
Output: 2, nums = [2, 2, _, _]

Input:  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Output: 5, nums = [0, 1, 3, 0, 4, _, _, _]
```

## Approach

Two-pointer / overwrite in-place:

- Maintain a write pointer `index` starting at 0.
- Iterate through every element with `i`.
- If `nums[i] != val`, copy it to `nums[index]` and advance `index`.
- Return `index` as the count of kept elements.

## Complexity

| | |
|---|---|
| Time | O(n) |
| Space | O(1) |
