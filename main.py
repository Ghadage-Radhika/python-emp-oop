# Main file
from permanent_employee import PermanentEmployee
from contract_employee import ContractEmployee
from intern import Intern

def main():
    employees = [
        PermanentEmployee("P123", "Alice Johnson", "IT", 60000, 5000),
        ContractEmployee("C456", "Bob Smith", "HR", 50, 160),
        Intern("I789", "Charlie Brown", "Finance", 1500)
    ]
    
    for employee in employees:
        employee.display_details()

if __name__ == "__main__":
    main()
