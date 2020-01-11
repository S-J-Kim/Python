import sys

input_file = "Three_bears.txt"

print("Output : BabyShark")

with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print(row.strip())