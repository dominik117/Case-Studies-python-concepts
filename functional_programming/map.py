def check_promotion_eligibility(employee):
    """
    Check if an employee is eligible for promotion based on years of experience.

    :param employee: A dictionary containing employee's data.
    :return: Updated employee record with promotion eligibility.
    """
    # Adding 'is_eligible' key based on years of experience
    employee['is_eligible'] = employee['years_of_experience'] > 5
    return employee

# Sample data: list of employee records
employees = [
    {'name': 'Alice', 'department': 'Engineering', 'years_of_experience': 4},
    {'name': 'Bob', 'department': 'Marketing', 'years_of_experience': 8},
    {'name': 'Charlie', 'department': 'Sales', 'years_of_experience': 5},
    {'name': 'Diana', 'department': 'Human Resources', 'years_of_experience': 7}
]

# Using map to apply the eligibility check
updated_employees = list(map(check_promotion_eligibility, employees))

# Display the updated employee records
for employee in updated_employees:
    print(employee)
