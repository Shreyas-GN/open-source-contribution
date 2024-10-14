import json  # Import the json library to handle JSON data
import csv   # Import the csv library to write data in CSV format

def json_to_csv(json_file, csv_file):
    """
    Converts a JSON file to a CSV file.
    
    Parameters:
    json_file (str): The path to the input JSON file.
    csv_file (str): The path to the output CSV file.
    """
    try:
        # Open the JSON file in read mode
        with open(json_file, 'r') as j_file:
            # Load the JSON data into a Python object
            data = json.load(j_file)

        # Open the CSV file in write mode, with newline='' to avoid extra blank lines
        with open(csv_file, 'w', newline='') as c_file:
            # Create a CSV writer object
            writer = csv.writer(c_file)
            
            # Check if data is not empty and write headers
            if data:
                writer.writerow(data[0].keys())  # Write the header row from the keys of the first dictionary
                
                # Write each entry's values to the CSV file
                for entry in data:
                    writer.writerow(entry.values())  # Write values of each entry
            
            print(f"Successfully converted {json_file} to {csv_file}.")
    
    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check if the file contains valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Prompt the user to enter the JSON file name
json_filename = input("Enter the JSON file name (with path if not in the same directory): ")
# Prompt the user to enter the desired output CSV file name
csv_filename = input("Enter the output CSV file name (with .csv extension): ")

# Call the conversion function
json_to_csv(json_filename, csv_filename)
