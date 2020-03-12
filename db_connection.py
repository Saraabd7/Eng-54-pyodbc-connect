import pyodbc

# make the connection
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Making the connection
conn = pyodbc.connect('DSN=MYMSSQL;UID='+username+';PWD='+password+';'+'DATABASE='+database)

# Creating a cursor object from connection
# Imagine like a real cursor on your azure data studio
# This will maintain state
crsr = conn.cursor()

# Running SQL Queries using .execute()
crsr.execute("select * FROM Customers")

# Cursor maintains state
# row = crsr.fetchone() # gets the next entry in the cursor
# print(row)
# row = crsr.fetchone() # gets the next entry in the cursor
# print(row)

# each row, has all the columns of that entry.
# getting individual data is easy from this row
# print(row.CompanyName)
# print(row.ContactName)
# print(row.Fax)

# Checking the headers of the columns
# print(crsr.description)
#
# print(type(crsr))
# print(type(crsr.fetchone()))

# using the .fetchall() # is dangerous
# Using fetchall is dangerous because you can stall/crash your servers
# if there is a lot of data :) and it will bottle neck the system
crsr.execute("select * FROM Customers")
all_rows = crsr.fetchall()
print(all_rows)
print(type(all_rows))

counter = 0
for item in all_rows:
    # print(item)
    print(counter,item.ContactName, '-', 'Fax:',  item.Fax)
    counter += 1

#   Best practices is to use a while loop and fetchone()
#  until your entry is none.
rows = crsr.execute("select * FROM Customers")

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.ContactName)


# another example of while loop with fetch one but or products table
rows = crsr.execute("SELECT * FROM Products")
new_values = []

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice * 200)
    new_values.append(record.UnitPrice * 200)

print(new_values)