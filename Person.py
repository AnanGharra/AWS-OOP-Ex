#!/usr/bin/env python3

class Person:
    "A class representing a person."
    def __init__(self, first_name, last_name, gender, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.height = height  # height in meters
        self.weight = weight  # weight in kilograms

    def get_info(self):
        "Return person's information as a dictionary."
        return {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Gender": self.gender,
            "Age": self.age,
            "Height": self.height,
            "Weight": self.weight
        }

    def calculate_bmi(self):
        "Calculate and return the Body Mass Index (BMI) of the person."
        return (self.weight) / ((self.height / 100) ** 2)
