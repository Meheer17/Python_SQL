# This file has all the various functions of SQL and also has a login feature, to ensure that an authenticated user can access the database. 

# SQL_FUNCTIONS

import mysql.connector # This is the required package to run the MYSQL COMMANDS

headers = [0,'COMMON'] # This is a list that holds a user authentication. 

mydb = mysql.connector.connect( # To establish the connection between python on MYSQL
    host="localhost",
    user="",            # Username to be entered here
    password="",        # Password for MYSQL
    database=headers[1] # Don't Change
)

mc = mydb.cursor() # The MYSQL CURSOR TO EXECUTE THE COMMANDS

# FUNCTIONS

# Codes for creating, deleting and modifying tables.

def Login():                            # This function is the most important function, without which none of the other codes work.
    name = input("Enter Username: ")
    pas = input("Enter the Password: ")
    mc.execute(f"USE {name};")
    mc.execute(f"SELECT * FROM password;")
    data = mc.fetchall()
    global headers
    for i in data:
        if i[0] == pas:
            headers = [1, name]
        else:
            mc.execute(f"USE COMMON;") 

def DisplayDatabase():                  # To get all the Database Names 
    if Auth():
        mc.execute("SHOW DATABASES;")
        data = mc.fetchall()
        for i in range(len(data)):
            print(f'{i + 1} - {data[i][0]}')
        print()
        return data

def SignUp():                           # Signup for a new User (Creating a new Database)
    database_name = input("Enter the Database Name to be Created: ")
    pas = input("Enter Your Password: ")
    mc.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")
    mc.execute(f"USE {database_name};")
    mc.execute(f"CREATE TABLE IF NOT EXISTS password(password varchar(100));")
    mc.execute(f"INSERT INTO password VALUES ('{pas}');")
    mydb.commit()
    print()
    Login()

def DropDatabase():                     # To drop a Database
    if Auth():
        data = DisplayDatabase()
        dd = int(input("Enter the Database to be Deleted (Number): "))
        mc.execute(f"DROP DATABASE {data[dd-1][0]}")

def Auth():                             # To check if the user has logged in or not
    if headers[0] == 1:
        return True
    else :
        return False

def ShowTable():                        # To display and send the Table datas thorughout the file
    if Auth():
        mc.execute("SHOW TABLES;")
        data = mc.fetchall()
        for i in range(len(data)):
            print(f'{i + 1} - {data[i][0]}')
        return data

def CreateTable():                      # Creating a table with Datatypes and Constraints (Complusory)
    if Auth():
        table_name = input("Enter the New Table's Name: ")
        nof = int(input("Enter the number of Columns: "))
        DataTypes = ['CHAR', 'VARCHAR', 'TEXT', 'INT', 'TINYINT', 'FLOAT', 'DATE', 'TIMESTAMP', 'SERIAL']

        c = []
        for i in range(nof):
            naof = input("\nEnter the name of the column: ")
            print()
            for j in range(len(DataTypes)):
                print(f'{j + 1} - {DataTypes[j]}')
            dt = tuple(input("Enter the DataType Number and value to be parsed with space: ").split(' '))
            if ((DataTypes[int(dt[0])-1] != "DATE") & (DataTypes[int(dt[0])-1] != "TIMESTAMP") & (DataTypes[int(dt[0])-1] != "SERIAL")):
                dt = (DataTypes[int(dt[0])-1], int(dt[1]))
                dt = f"{dt[0]}({dt[1]})"
            else:
                dt = f"{DataTypes[int(dt[0])-1]}"
            
            cons = Constraint()
            txt = f"{naof} {dt} {cons}"
            c.append(txt)
            tet = ",".join(c)
        mc.execute(f"CREATE TABLE {table_name}({tet});")

def DesTable():                         # Desc Table_Name
    if Auth():
        data = ShowTable()
        T_N = int(input("Enter the Table Number to Show Details: "))
        mc.execute(f"DESC {data[T_N - 1][0]};")
        det = mc.fetchall()
        print("| Field | Type | Null | Key | Default | Extra |")
        for i in det:
            print(i)
        return (det, data, T_N)

def Rename():                           # To change the name of the Table
    if Auth():
        data = ShowTable()
        print("\nWhich Column Name to Change:-")
        for i in range(len(data)):
            print(f'{i + 1} - {data[i][0]}')
        rn = int(input("Enter the Table Num you want to change: "))
        rnn = input("Enter the name you want to rename to: ")
        if data[rn-1][0] != 'password':
            mc.execute(f"ALTER TABLE {data[rn -1][0]} RENAME TO {rnn}")

def DropTable():
    if Auth():                          # Drop the table from the database
        data = ShowTable()
        print("\nWhich Column Name to Change:-")
        for i in range(len(data)):
            print(f'{i + 1} - {data[i][0]}')
        dt = int(input("Enter the table to delete: "))
        if data[dt-1][0] != 'password':
            mc.execute(f"DROP TABLE {data[dt-1][0]}")
        
def ADMTable():                         # ADD, DELETE AND MODIFY COLUMNS IN A TABLE
    if Auth():
        types = ["ADD","DROP","MODIFY"]
        print()
        data = DesTable()
        print()
        for i in range(len(types)):
            print(f"{i+1} - {types[i]} Column")
        ch = int(input("Enter the Task: "))
        if((ch == 1) | (ch == 2) | (ch == 3)):
            if ch ==1:
                DataTypes = ['CHAR', 'VARCHAR', 'TEXT', 'INT', 'TINYINT', 'FLOAT', 'DATE', 'TIMESTAMP', 'SERIAL']
                naof = input("\nEnter the name of the column: ")
                print()
                for j in range(len(DataTypes)):
                    print(f'{j + 1} - {DataTypes[j]}')
                dt = tuple(input("Enter the DataType Number and value to be parsed with space: ").split(' '))
                if ((DataTypes[int(dt[0])-1] != "DATE") & (DataTypes[int(dt[0])-1] != "TIMESTAMP") & (DataTypes[int(dt[0])-1] != "SERIAL")):
                    dt = (DataTypes[int(dt[0])-1], int(dt[1]))
                    dt = f"{dt[0]}({dt[1]})"
                else:
                    dt = f"{DataTypes[int(dt[0])-1]}"

                txt = f"{naof} {dt}"
                mc.execute(f'ALTER TABLE {data[1][data[2] -1][0]} ADD {txt};')
            if ch == 2:
                for i in range(len(data[0])):
                    print(f"{i + 1} - {data[0][i][0]}")
                drope = int(input("Enter the column to DELETE: "))
                mc.execute(f'ALTER TABLE {data[1][data[2] -1][0]} DROP { data[0][drope - 1][0]};')
            if ch == 3:
                DataTypes = ['CHAR', 'VARCHAR', 'TEXT', 'INT', 'TINYINT', 'FLOAT', 'DATE', 'TIMESTAMP', 'SERIAL']
                for i in range(len(data[0])):
                    print(f"{i + 1} - {data[0][i][0]}")
                drope = int(input("Enter the column to MODIFY: "))
                for j in range(len(DataTypes)):
                    print(f'{j + 1} - {DataTypes[j]}')
                dt = tuple(input("Enter the DataType Number and value to be parsed with space: ").split(' '))
                if ((DataTypes[int(dt[0])-1] != "DATE") & (DataTypes[int(dt[0])-1] != "TIMESTAMP") & (DataTypes[int(dt[0])-1] != "SERIAL")):
                    dt = (DataTypes[int(dt[0])-1], int(dt[1]))
                    dt = f"{dt[0]}({dt[1]})"
                else:
                    dt = f"{DataTypes[int(dt[0])-1]}"

                txt = f"{dt}"
                
                cons = input("Do you want to add constraints? (Y/N): ")
                if cons.upper() == "Y":
                    text = Constraint()
                    mc.execute(f'ALTER TABLE {data[1][data[2] -1][0]} MODIFY { data[0][drope - 1][0]} {txt} {text};')
                else: 
                    mc.execute(f'ALTER TABLE {data[1][data[2] -1][0]} MODIFY { data[0][drope - 1][0]} {txt};')
        
def Constraint():                       # Used as a function to send the text for the constraints while making a TABLE and its details
    constraints = ["NOT NULL", "DEFAULT", "UNIQUE", "PRIMARY KEY", "CHECK","FOREIGN KEY"]
    for i in range(len(constraints)):
        print(f'{i + 1} - {constraints[i]}')
    c = int(input("Enter the constraint: "))
    if((c == 5) | (c == 6)):
        if c == 5:
            con = input("Enter Your Condition: ")
            text = f"CHECK({con})"
        if c == 6:
            tn = input("Enter the table name: ")
            cn = input("Enter the column name to be refered: ")
            text = f"FOREIGN KEY REFERENCES {tn}({cn})"
    else:
        text = f"{constraints[c - 1]}"
    return text

# Codes for displaying content.

def DisplayAll():                          # SELECT * FROM TABLE_NAME
    if Auth():
        data = ShowTable()
        ta = int(input("Enter the table num you want to access: "))
        mc.execute(F"SELECT * FROM {data[ta -1][0]}")
        for i in mc.description:
            print(i[0], end="   ")
        data = mc.fetchall()
        for i in data:
            print()
            for j in i:
                print(j, end="     ")
        
def DisplayWithWhere():                     # SELECT * FROM TABLE NAME WHERE <CONDITION>
    if Auth():
        data = ShowTable()
        ta = int(input("Enter the table num you want to access: "))
        cond = input("Enter the condition (WHERE METHOD): ")
        mc.execute(F"SELECT * FROM {data[ta -1][0]} WHERE {cond};")
        for i in mc.description:
            print(i[0], end="   ")
        data = mc.fetchall()
        for i in data:
            print()
            for j in i:
                print(j, end="     ")

def DisplayOrderBy():                       # SELECT * FROM TABLE_NAME ORDER BY COLUMN_NAME
    if Auth():
        data = DesTable()
        ta = input("Enter the column name to order with: ")
        ob = input("Enter the method to order by (asc/desc): ")
        mc.execute(F"SELECT * FROM {data[1][data[2]-1][0]} ORDER BY {ta} {ob};")
        for i in mc.description:
            print(i[0], end="   ")
        data = mc.fetchall()
        for i in data:
            print()
            for j in i:
                print(j, end="     ")

def DisplayGroupBy():                       # SELECT * FROM TABLE_NAME GROUP BY COLUMN_NAME
    if Auth():
        data = DesTable()
        ta = input("Enter the column name to group with: ")
        mc.execute(F"SELECT * FROM {data[1][data[2]-1][0]} GROUP BY {ta};")
        for i in mc.description:
            print(i[0], end="   ")
        data = mc.fetchall()
        for i in data:
            print()
            for j in i:
                print(j, end="     ")

def CustomQuery():                          # TO WRITE A USER DEFINED QUERY TO GET THEIR MOST FAVORABLE OUTPUT `SELECT <USER QUERY>`
    if Auth():
        code = input("Enter Your Query Here (After SELECT): ")
        mc.execute(f"SELECT {code} ;")
        for i in mc.description:
            print(i[0], end="   ")
        data = mc.fetchall()
        for i in data:
            print()
            for j in i:
                print(j, end="     ")


# Update Function

def Update():                               # TO UPDATE THE RECORDS BY THE USER ITSELF BY PASSING THE QUERY
    if Auth():
        data = DesTable()
        print()
        for i in range(len(data[0])):
            print(f"{i + 1} - {data[0][i][0]}")
        table = data[1][data[2]-1][0]
        wtu = input("Add your query here (Enter Your whole Query just as how you want to update with or witohut the WHERE CLAUS): ")
        mc.execute(f"UPDATE {table} SET {wtu};")