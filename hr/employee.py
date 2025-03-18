from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name, department):
        self._employee_id = employee_id  # Encapsulation
        self._name = name
        self._department = department
    
    @abstractmethod
    def calculate_salary(self):
        pass
    
    def display_details(self):
        print("--- Employee Details ---")
        print(f"Employee ID: {self._employee_id}")
        print(f"Name: {self._name}")
        print(f"Department: {self._department}")
