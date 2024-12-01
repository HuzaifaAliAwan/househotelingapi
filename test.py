
import os

# Read locations from file
try:
    with open("test.txt", "r") as f:
        locations = set(f.read().splitlines())
except FileNotFoundError:
    print("Error: File 'test.txt' not found.")
    exit(1)

# Define seasons
seasons = ['summer', 'winter', 'autumn', 'spring']

# Combine locations and seasons
combined_list = []
for location in locations:
    for season in seasons:
        combined_list.append(f"['{location.lower()}','{season}'],")

# Write combined data to file
try:
    with open("combinedData.txt", "w") as f:
        # for item in combined_list:
        #     f.write(item + "\n")
        f.writelines(combined_list)
except IOError as e:
    print(f"Error writing to file: {e}")
    exit(1)

print("Combined data written to file.")
