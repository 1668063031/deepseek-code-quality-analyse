# Maximum Containers on a Ship
# Original code: class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        

Here's a Python3 solution using a functional approach to solve the problem of determining the maximum number of containers that can be loaded onto an n x n deck without exceeding the ship's maximum weight capacity:

```python
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        total_cells = n * n
        max_possible = maxWeight // w
        return min(total_cells, max_possible)
```

### Explanation:
1. **Calculate Total Cells**: The total number of cells on the deck is `n * n` since the deck is an n x n grid.
2. **Determine Maximum Containers by Weight**: The maximum number of containers that can be loaded without exceeding `maxWeight` is found by integer division of `maxWeight` by the weight of each container `w` (i.e., `maxWeight // w`).
3. **Return the Minimum**: The result is the smaller of the two values: the total number of cells on the deck or the maximum number of containers allowed by the weight constraint. This ensures we do not exceed either the physical space or the weight limit.

This approach efficiently computes the solution in constant time O(1) by leveraging basic arithmetic operations.