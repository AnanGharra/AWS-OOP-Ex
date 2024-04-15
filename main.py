#!/usr/bin/env python3

from Circle import Circle
from Square import Square
from Card import Deck
from Person import Person
from RomanNumerals import RomanNumerals
from ParenthesesValidator import ParenthesesValidator
from Subsets import Subsets
from PairFinder import PairFinder
from ThreeSumZero import ThreeSumZero
from StringProcessor import StringProcessor

circle = Circle(5)
print("Area of circle:", circle.area())  # Expected output: Area of circle: 78.53981633974483
print("Perimeter of circle:", circle.perimeter())  # Expected output: Perimeter of circle: 31.41592653589793


square = Square(4)
print("Area of square:", square.area())  # Expected output: Area of square: 16
print("Perimeter of square:", square.perimeter())  # Expected output: Perimeter of square: 16


deck = Deck()
deck.shuffle()
print("First card dealt:", deck.deal())  # Example output: First card dealt: Card(suit='Hearts', value='2')
print("Second card dealt:", deck.deal())  # Example output: Second card dealt: Card(suit='Clubs', value='K')


person = Person("Dan", "Will", "Male", 30, 175, 70)
print("Person info:", person.get_info())  
# Expected output: Person info: {'first_name': 'John', 'last_name': 'Doe', 'gender': 'Male', 'age': 30, 'height': 175, 'weight': 70}
print("BMI:", person.bmi())  # Expected output: BMI: 22.857142857142858



# Create a person who also has a job information embedded
alice = Person("Alice", "Smith", "Female", 29, 165, 60, "TechCorp", 40, "Manager")
bob = Person("Bob", "Jones", "Male", 45, 175, 80, "MoneyBank", 50, "Analyst")

print(alice)
print(bob)


converter = RomanNumerals()
print("Integer to Roman:", converter.to_roman(1994))  # Expected output: Integer to Roman: MCMXCIV
print("Roman to Integer:", converter.to_int('MCMXCIV'))  # Expected output: Roman to Integer: 1994
print("Integer to Roman:", converter.to_roman(58))  # Expected output: Integer to Roman: LVIII
print("Roman to Integer:", converter.to_int('LVIII'))  # Expected output: Roman to Integer: 58


validator = ParenthesesValidator()
print(validator.is_valid("()[]{}"))  # Expected output: True
print(validator.is_valid("({[)]"))   # Expected output: False
print(validator.is_valid("[()]{}{[()()]()}"))  # Expected output: True
print(validator.is_valid("[(])"))  # Expected output: False


subsets = Subsets()
print(subsets.all_subsets([4, 5, 6]))  
# Expected output: [[], [4], [4, 5], [4, 5, 6], [4, 6], [5], [5, 6], [6]]


finder = PairFinder()
print(finder.find_pair([10, 20, 10, 40, 50, 60, 70], 50))  # Expected output: (2, 3)
print(finder.find_pair([1, 2, 3, 4, 5], 9))  # Expected output: (3, 4)
print(finder.find_pair([1, 2, 3, 4, 5], 10))  # Expected output: None


three_sum_zero = ThreeSumZero()
print(three_sum_zero.find_triplets([-25, -10, -7, -3, 2, 4, 8, 10]))  
# Expected output: [[-10, 2, 8], [-7, -3, 10]]
print(three_sum_zero.find_triplets([-1, 0, 1, 2, -1, -4]))  
# Expected output: [[-1, -1, 2], [-1, 0, 1]]


processor = StringProcessor()
processor.get_string()      # Simulating input: hello world
processor.print_string()    # Expected output: HELLO WORLD
processor.get_string()      # Simulating input: testing again
processor.print_string()    # Expected output: TESTING AGAIN
