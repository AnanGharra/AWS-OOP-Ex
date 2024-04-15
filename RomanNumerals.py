#!/usr/bin/env python3


class RomanNumerals:
    "Class to convert between Roman numerals and integers."
    roman_to_int_mapping = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    int_to_roman_mapping = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
        90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    @staticmethod
    def to_roman(value):
        result = []
        # Ensure that we sort by the integer keys in descending order
        for integer, roman in sorted(RomanNumerals.int_to_roman_mapping.items(), key=lambda x: x[0], reverse=True):
            while value >= integer:
                result.append(roman)
                value -= integer
        return ''.join(result)

    @staticmethod
    def to_int(roman):
        result = 0
        i = 0
        while i < len(roman):
            if (i + 1 < len(roman)) and (RomanNumerals.roman_to_int_mapping[roman[i]] < RomanNumerals.roman_to_int_mapping[roman[i+1]]):
                result += RomanNumerals.roman_to_int_mapping[roman[i+1]] - RomanNumerals.roman_to_int_mapping[roman[i]]
                i += 2
            else:
                result += RomanNumerals.roman_to_int_mapping[roman[i]]
                i += 1
        return result

