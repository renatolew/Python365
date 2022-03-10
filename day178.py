# Create a function with default argument


def show_employee(name, salary=7500):
    print("Name:", name, "- Salary:", salary)

show_employee("Renato", 10000)
show_employee("João")
show_employee("Maria", 5000)