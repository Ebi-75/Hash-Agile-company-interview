# Sample employee records
employee_records = [
    {'id': 'E02001', 'Name': 'mary', 'Department': 'IT', 'Gender': 'Female'},
    {'id': 'E02002', 'Name': 'kumar', 'Department': 'HR', 'Gender': 'Male'},
    {'id': 'E02003', 'Name': 'vijay', 'Department': 'IT', 'Gender': 'Male'},
    {'id': 'E02004', 'Name': 'geetha', 'Department': 'Finance', 'Gender': 'Female'},
    {'id': 'E02005', 'Name': 'eva', 'Department': 'Data Science', 'Gender': 'Female'},
    {'id': 'E02006', 'Name': 'Ebinesh', 'Department': 'Data Science', 'Gender': 'Male'},
]

# Dictionary to store collections
employee_data = {}


def createCollection(p_collection_name):
    """Create a new collection."""
    if p_collection_name in employee_data:
        print(f"Collection '{p_collection_name}' already exists.")
    else:
        employee_data[p_collection_name] = []
        print(f"Collection '{p_collection_name}' created successfully.")


def indexData(p_collection_name, p_exclude_column):
    """Index employee data into the specified collection, excluding a specific column."""
    if p_collection_name not in employee_data:
        print(f"Collection '{p_collection_name}' does not exist. Please create it first.")
        return

    for record in employee_records:
        indexed_record = {k: v for k, v in record.items() if k != p_exclude_column}
        employee_data[p_collection_name].append(indexed_record)
    print(f"Data indexed into collection '{p_collection_name}' excluding column '{p_exclude_column}'.")


def searchByColumn(p_collection_name, p_column_name, p_column_value):
    """Search for records where a specific column matches a given value."""
    if p_collection_name not in employee_data:
        print(f"Collection '{p_collection_name}' does not exist.")
        return []

    results = []
    for record in employee_data[p_collection_name]:
        if record.get(p_column_name) == p_column_value:
            results.append(record)

    return results


def getEmpCount(p_collection_name):
    """Get the count of employees in the specified collection."""
    if p_collection_name not in employee_data:
        print(f"Collection '{p_collection_name}' does not exist.")
        return 0

    count = len(employee_data[p_collection_name])
    print(f"Employee count in collection '{p_collection_name}': {count}")
    return count


def delEmpById(p_collection_name, p_employee_id):
    """Delete an employee by their ID from the specified collection."""
    if p_collection_name not in employee_data:
        print(f"Collection '{p_collection_name}' does not exist.")
        return

    initial_count = len(employee_data[p_collection_name])
    employee_data[p_collection_name] = [
        record for record in employee_data[p_collection_name] if record.get('id') != p_employee_id
    ]
    final_count = len(employee_data[p_collection_name])

    if initial_count == final_count:
        print(f"Employee with ID '{p_employee_id}' not found in collection '{p_collection_name}'.")
    else:
        print(f"Employee with ID '{p_employee_id}' has been deleted from collection '{p_collection_name}'.")


def getDepFacet(p_collection_name):
    """Retrieve the count of employees grouped by department from the specified collection."""
    if p_collection_name not in employee_data:
        print(f"Collection '{p_collection_name}' does not exist.")
        return {}

    department_count = {}
    for record in employee_data[p_collection_name]:
        department = record.get('Department')
        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1

    return department_count


# Define collection names
v_nameCollection = 'Hash_EbineshK'
v_phoneCollection = 'Hash_7405'

# Create collections
createCollection(v_nameCollection)
createCollection(v_phoneCollection)

# Index data into the name collection without excluding any columns for department searches
indexData(v_nameCollection, 'Gender')  # Exclude Gender for this collection

# Example usage
count_name_collection = getEmpCount(v_nameCollection)
print("Employee count in name collection:", count_name_collection)

# Search examples
it_employees = searchByColumn(v_nameCollection, 'Department', 'IT')
print("Employees in IT department:", it_employees)

# Delete an employee by ID
delEmpById(v_nameCollection, 'E02005')  # Deleting Eva
print("Updated Employee count in name collection after deletion:", getEmpCount(v_nameCollection))

# Get department facet counts
department_counts = getDepFacet(v_nameCollection)
print("Department counts:", department_counts)
