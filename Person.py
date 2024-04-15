#!/usr/bin/env python3

from WorkPlace import Job

class Person(Job):
    "A class representing a person."
    def __init__(self, first_name, last_name, gender, age, height, weight, name=None, pay_rate=None, position=None):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.height = height  # height in meters
        self.weight = weight  # weight in kilograms
        self.name = name
        self.pay_rate = pay_rate
        self.position = position

    def get_info(self):
        "Return person's information as a dictionary."
        info = {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Gender": self.gender,
            "Age": self.age,
            "Height": self.height,
            "Weight": self.weight,
        }
        if self.position is not None:
            info['Position'] = self.position
        if self.name is not None:
            info['Work Place'] = self.name
        return info


    def bmi(self):
        "Calculate and return the Body Mass Index (BMI) of the person."
        return (self.weight) / ((self.height / 100) ** 2)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.position} at {self.name}"
