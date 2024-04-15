#!/usr/bin/env python3


class Subsets:
    "Class to generate all possible unique subsets of a list of distinct integers."
    
    def all_subsets(self, nums):
        result = []
        self._backtrack(sorted(nums), [], result, 0)
        return result
    
    def _backtrack(self, nums, current, result, start):
        result.append(list(current))
        for i in range(start, len(nums)):
            current.append(nums[i])
            self._backtrack(nums, current, result, i + 1)
            current.pop()


