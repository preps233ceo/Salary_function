# Load necessary libraries
library(readr)
library(zip)

# Define the path to the zip file
zip_file <- "Employee_Profile.zip"

# Unzip the file into a directory
unzip(zip_file, exdir = "C:\Users\Admin\Desktop")

# List files in the directory
file_list <- list.files("Employee_Profile", full.names = TRUE)

# Read and display each file
for (file in file_list) {
  data <- read_csv(file)
  print(data)
}

# Clean up: remove unzipped files after displaying
unlink("Employee_Profile", recursive = TRUE)

