#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import zipfile
import pandas as pd


# Import the salary data into a pandas DataFrame
salary_data = pd.read_csv('Total.csv')

# Display the first few rows of the DataFrame to verify the data has been imported correctly
salary_data.head()



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

# Example1
export_employee_details_to_csv("NATHANIEL FORD")
# Example2
export_employee_details_to_csv("NATHANIEL")


# In[ ]:




