#!/usr/bin/env python3


class PairFinder:
    "Class to find a pair of elements from a given array whose sum equals a specific target number."
    
    def find_pair(self, numbers, target):
        lookup = {}
        for index, number in enumerate(numbers):
            complement = target - number
            if complement in lookup:
                return complement, number
            lookup[number] = index
        return None

