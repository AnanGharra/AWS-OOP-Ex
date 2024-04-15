#!/usr/bin/env python3


class ParenthesesValidator:
    "Class to check the validity of a string of parentheses."
    
    @staticmethod
    def is_valid(s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack  # Return True if stack is empty (valid), else False
