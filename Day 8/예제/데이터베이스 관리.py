#!/usr/bin/env python3
import sqlite3

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:')  # 경로를 지정하면 sql파일로 생성할 수도 있음
query = """CREATE TABLE sales
			(customer VARCHAR(20), 
			 product VARCHAR(40),
			 amount FLOAT,
			 date DATE);"""
con.execute(query)  # SQL 명령어를 실행한다
con.commit()        # 수정된 내용을 적용시킨다 (업데이트)

# Insert a few rows of data into the table
data = [('Richard Lucas', 'Notepad', 2.50, '2019-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2019-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2019-02-03'),
        ('Stephen Randolph', 'Computer', 679.40, '2019-02-20')]
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

# Query the sales table
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# Count the number of rows in the output
row_counter = 0
for row in rows:
	print(row)
	row_counter += 1
print('Number of rows: {}'.format(row_counter))
