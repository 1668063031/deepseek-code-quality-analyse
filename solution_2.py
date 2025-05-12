# Unique 3-Digit Even Numbers
# Original code: class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        

To solve this problem, we need to determine the number of distinct three-digit even numbers that can be formed using the given digits, where each digit can be used only once per number (unless there are duplicates in the input array), and there are no leading zeros. 

### Approach
1. **Generate all possible permutations**: We need to consider all possible three-digit combinations from the given digits. Since the order matters (123 is different from 321), permutations are suitable here. However, since digits can be repeated in the input array, we need to handle duplicates properly.
2. **Check for validity**: Each permutation must meet the following criteria:
   - **Three-digit number**: The first digit (hundreds place) cannot be zero.
   - **Even number**: The last digit (units place) must be even (0, 2, 4, 6, or 8).
   - **Unique combinations**: Even if digits are repeated in the input, each combination must be considered only once. For example, with digits [0, 2, 2], the valid numbers are 202 and 220, and permutations like 220 and 202 are distinct.
3. **Count distinct valid numbers**: After generating all valid permutations, we need to count the distinct numbers formed.

### Solution Code
```python
from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_numbers = set()
        for p in permutations(digits, 3):
            if p[0] != 0 and p[2] % 2 == 0:
                num = p[0] * 100 + p[1] * 10 + p[2]
                unique_numbers.add(num)
        return len(unique_numbers)
```

### Explanation
1. **Generating Permutations**: The `permutations` function from the `itertools` module is used to generate all possible 3-length permutations of the digits. This handles the selection of digits in all possible orders without replacement (each digit in the permutation is unique in position, even if the same digit appears multiple times in the input array).
2. **Checking Validity**: For each permutation, we check two conditions:
   - **No Leading Zero**: The first digit (hundreds place) must not be zero to form a valid three-digit number.
   - **Even Number**: The last digit (units place) must be even (0, 2, 4, 6, or 8).
3. **Storing Unique Numbers**: Valid permutations are converted into three-digit numbers and added to a set to automatically handle duplicates, ensuring only distinct numbers are counted.
4. **Result**: The size of the set gives the count of distinct valid three-digit even numbers that can be formed.

This approach efficiently checks all possible permutations, filters valid numbers, and uses a set to ensure uniqueness, providing the correct count of distinct three-digit even numbers.