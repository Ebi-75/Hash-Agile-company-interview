import pandas as pd

# Load the employee CSV file
file_path = 'Employee Sample Data 1.csv'  # Ensure this is the correct path to your CSV file
df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Adjust encoding if needed

# In-memory collections to mimic a database
collections = {}

# Function Definitions
def createCollection(p_collection_name):
    collections[p_collection_name] = []
    print(f"Collection '{p_collection_name}' created.")

def indexData(p_collection_name, p_exclude_column):
    collection = collections.get(p_collection_name)
    if collection is not None:
        for index, row in df.iterrows():
            employee_data = row.to_dict()
            employee_data.pop(p_exclude_column, None)  # Exclude the specified column
            collections[p_collection_name].append(employee_data)
        print(f"Indexed data into '{p_collection_name}' excluding '{p_exclude_column}'.")

def searchByColumn(p_collection_name, p_column_name, p_column_value):
    collection = collections.get(p_collection_name)
    if collection:
        results = [emp for emp in collection if emp.get(p_column_name) == p_column_value]
        return results
    return []

def getEmpCount(p_collection_name):
    collection = collections.get(p_collection_name)
    if collection is not None:
        return len(collection)
    return 0

def delEmpById(p_collection_name, p_employee_id):
    collection = collections.get(p_collection_name)
    if collection:
        collections[p_collection_name] = [emp for emp in collection if emp.get('Employee ID') != p_employee_id]
        print(f"Employee with ID '{p_employee_id}' deleted from '{p_collection_name}'.")

def getDepFacet(p_collection_name):
    collection = collections.get(p_collection_name)
    if collection:
        dep_count = {}
        for emp in collection:
            department = emp.get('Department')
            if department:
                dep_count[department] = dep_count.get(department, 0) + 1
        return dep_count
    return {}

# Execute the required functions with the dataset

# Replace with your actual name and phone last four digits
v_nameCollection = 'Hash_YourName'
v_phoneCollection = 'Hash_1234'

# 1. Create collections
createCollection(v_nameCollection)
createCollection(v_phoneCollection)

# 2. Get employee count before indexing
initial_count_name = getEmpCount(v_nameCollection)

# 3. Index data into both collections
indexData(v_nameCollection, 'Department')
indexData(v_phoneCollection, 'Gender')

# 4. Delete an employee by ID
delEmpById(v_nameCollection, 'E02003')

# 5. Get employee count after deletion
final_count_name = getEmpCount(v_nameCollection)

# 6. Search by columns
it_employees_name = searchByColumn(v_nameCollection, 'Department', 'IT')
male_employees_name = searchByColumn(v_nameCollection, 'Gender', 'Male')
it_employees_phone = searchByColumn(v_phoneCollection, 'Department', 'IT')

# 7. Get department facet
dep_facet_name = getDepFacet(v_nameCollection)
dep_facet_phone = getDepFacet(v_phoneCollection)

# Collecting results for output
output_results = {
    "Initial Employee Count": initial_count_name,
    "Final Employee Count": final_count_name,
    "IT Employees (Name Collection)": it_employees_name,
    "Male Employees (Name Collection)": male_employees_name,
    "IT Employees (Phone Collection)": it_employees_phone,
    "Department Facet (Name Collection)": dep_facet_name,
    "Department Facet (Phone Collection)": dep_facet_phone
}

# Print results for documentation
for key, value in output_results.items():
    print(f"{key}: {value}")
