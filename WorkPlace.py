#!/usr/bin/env python3

class WorkPlace:
    "A class representing a generic workplace."
    def __init__(self, name):
        self.name = name

    def calculate_salary(self, hours):
        raise NotImplementedError("This method should be overridden by subclasses")

class Job(WorkPlace):
    "A class representing a specific job position."
    def __init__(self, name, pay_rate, position):
        super().__init__(name)
        self.pay_rate = pay_rate
        self.position = position

    def calculate_salary(self, hours):
        base_salary = hours * self.pay_rate
        return base_salary * 3 if self.is_manager() else base_salary

    def is_manager(self):
        return "Manager" in self.position

    def __str__(self):
        return f"{self.position} at {self.name}, Pay Rate: {self.pay_rate}/hr"

# Creating specific job positions
class IT(Job):
    def __init__(self, name, position):
        super().__init__(name, 40, position)

class Finance(Job):
    def __init__(self, name, position):
        super().__init__(name, 50, position)

class HQ(Job):
    def __init__(self, name, position):
        super().__init__(name, 100, position)
