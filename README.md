# Salary_function
Python salary function that retrieves employee data from a data frame and stores it as a zip file and an R code for unzipping.
# Employee Salary Data Management

This project consists of a Python script designed to handle employee salary data. It imports salary data from a CSV file, retrieves details for a specified employee, and exports those details to a zipped CSV file. This README provides an overview of the code, its functions, and instructions for usage. An R script is included to unzip the zipped CSV file.

## Requirements

- Python 3.x
- Pandas
- Zipfile
- OS

You can install the necessary Python packages using:

```bash
pip install pandas
```

## Files

- `Total.csv`: A CSV file containing employee salary data.
- `employee_details.py`: The main script containing the code.

## Code Overview

### Importing Libraries

```python
import os
import zipfile
import pandas as pd
```

### Loading the Data

The salary data is loaded into a Pandas DataFrame from a CSV file named `Total.csv`.

```python
# Import the salary data into a pandas DataFrame
salary_data = pd.read_csv('Total.csv')

# Display the first few rows of the DataFrame to verify the data has been imported correctly
salary_data.head()
```

### Functions

#### `get_employee_details(employee_name)`

This function retrieves the details of an employee given their name. It returns the details as a dictionary if the employee is found, otherwise, it raises an appropriate error and returns `None`.

```python
def get_employee_details(employee_name):
    try:
        # Retrieve the employee details
        employee_details = salary_data[salary_data['EmployeeName'] == employee_name]
        
        # Check if any details were found
        if not employee_details.empty:
            # Convert the details to a dictionary format
            salary_dict = employee_details.to_dict(orient='records')[0]  # get the first (and only) dictionary in the list
            return salary_dict
        else:
            raise ValueError(f"Employee {employee_name} not found.")
    
    except ValueError as ve:
        print(ve)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
```

#### `export_employee_details_to_csv(employee_name)`

This function exports the details of an employee to a CSV file and then zips the file. It calls the `get_employee_details` function to retrieve the data.

```python
def export_employee_details_to_csv(employee_name):
    details = get_employee_details(employee_name)
    if details is not None:
        # Create a DataFrame from the details dictionary
        employee_df = pd.DataFrame([details])
        
        # Define the CSV and ZIP file names
        csv_filename = f"{employee_name.replace(' ', '_')}.csv"
        zip_filename = "Employee_Profile.zip"
        
        # Export details to CSV
        employee_df.to_csv(csv_filename, index=False)
        
        # Zip the CSV file
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(csv_filename)
        
        # Remove the CSV file after zipping
        os.remove(csv_filename)
        
        print(f"Details for {employee_name} exported and zipped successfully.")
    else:
        print(f"Could not export details for {employee_name}.")
```

### Example Usage

Two examples of how to use the `export_employee_details_to_csv` function are provided:

```python
# Example1. This results in an exported file.
export_employee_details_to_csv("NATHANIEL FORD")
# Example2. This results in an error.
export_employee_details_to_csv("NATHANIEL")
```

## Running the Code

1. Ensure `Total.csv` is in the same directory as the script.
2. Run the script using Python:

```bash
python employee_details.py
```

3. Call the `export_employee_details_to_csv` function with the desired employee name to export their details.

## Error Handling

- The `get_employee_details` function handles cases where the employee name is not found and prints an appropriate message.
- Both functions handle unexpected errors gracefully and print relevant error messages.

## Conclusion

This script provides a straightforward way to manage and export employee salary details from a CSV file. It includes error handling and example usage for easy integration into larger projects or for standalone use.
