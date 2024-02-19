import os
import csv

# Open the input CSV file and create a reader object
raw_data = os.path.join("data", "exam_score.csv")
with open(raw_data, "r") as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

# Determine the indices of the columns to be deleted
header = data[0]
indices_to_delete = [
    header.index(column_name) for column_name in ["# Level 3+4", "% Level 3+4"]
]

# Delete the specified columns from each row
for row in data:
    for index in sorted(indices_to_delete, reverse=True):
        del row[index]

# Write the modified data to a new CSV file
with open("clean_data.csv", "w", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerows(data)
