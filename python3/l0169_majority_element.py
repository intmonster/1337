from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            count += (1 if n == candidate else -1)
0        
        return candidate

