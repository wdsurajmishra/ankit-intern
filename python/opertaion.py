employees = []
class Management:
    
    def add_employee(name, role):
        """Add an employee to the system."""
        if name and role:
            employees.append({"name": name, "role": role})
            mgs = f"Employee {name} with role {role} added successfully."
            return mgs

        else:
            msg = "Name and role cannot be empty."
            return msg

    def list_employees():
        """List all employees in the system."""
        if employees:
            msg = "Employees in the system:\n"
            for emp in employees:
                msg += f"- {emp['name']} ({emp['role']})\n"
            return msg.strip()
        else:
            msg = "No employees found."
            return msg      

import os 