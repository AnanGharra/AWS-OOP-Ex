#!/usr/bin/env python3


class StringProcessor:
    "Class which can get a string from the user and print it in upper case."
    
    def __init__(self):
        self.input_string = ""
    
    def get_string(self):
        self.input_string = input("Enter a string: ")
    
    def print_string(self):
        print(self.input_string.upper())



