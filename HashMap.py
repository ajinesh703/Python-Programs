# Big hashmap for company structure
company = {
    'Engineering': {
        'employees': {
            'John': {'role': 'Senior Engineer', 'age': 35, 'experience': 10},
            'Sarah': {'role': 'Junior Engineer', 'age': 28, 'experience': 3}
        },
        'budget': 1500000
    },
    'Marketing': {
        'employees': {
            'Tom': {'role': 'Marketing Head', 'age': 40, 'experience': 15},
            'Jerry': {'role': 'Content Manager', 'age': 32, 'experience': 7}
        },
        'budget': 800000
    },
    'Sales': {
        'employees': {
            'Annie': {'role': 'Sales Executive', 'age': 29, 'experience': 5},
            'Jack': {'role': 'Sales Representative', 'age': 27, 'experience': 4}
        },
        'budget': 500000
    }
}

# Printing company structure
for department, details in company.items():
    print(f"Department: {department}")
    print(f"  Budget: ${details['budget']}")
    print("  Employees:")
    for employee, info in details['employees'].items():
        print(f"    {employee} - {info['role']}, Age: {info['age']}, Experience: {info['experience']} years")
    print()

# Example: Increase budget of Engineering department
company['Engineering']['budget'] += 200000
print("\nUpdated Budget for Engineering:", company['Engineering']['budget'])
