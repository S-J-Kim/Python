#!/usr/bin/env python3
import csv
import sqlite3
import sys

# Path to and name of a CSV input file
input_file = sys.argv[1]

# Create an in-memory SQLite3 database
# Create a table called Suppliers with five attributes
con = sqlite3.connect('bicycle.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS bicycle
				(aa varchar(40),
				bb int,
				cc varchar(50),
				dd varchar(90),
				ee float,
				ff float,
				gg varchar(30),
				hh int);"""
c.execute(create_table)
con.commit()

# Read the CSV file
# Insert the data into the Suppliers table
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		data.append(row[column_index])
	print(data)
	c.execute("INSERT INTO bicycle VALUES (?, ?, ?, ?, ?, ?, ?, ?);", data)
con.commit()

# Query the Suppliers table
output = c.execute("SELECT * FROM bicycle")
rows = output.fetchall()
for row in rows:
	output = []
	for column_index in range(len(row)):
		output.append(str(row[column_index]))
	print(output)
