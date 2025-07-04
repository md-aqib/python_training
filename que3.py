# Database and Employee Management

# Scenario: You are working on an HR management system.

# Write a Python program to:

# 1.   Connect to an SQLite database and create a table Employee with the following columns:

# id (Employee ID)
# name (Employee Name)
# email (Email Address)
# role (e.g., Developer, Manager, etc.)
# salary
# 2.   Insert at least 5 employee records into the table.

# 3.   Retrieve and display all employees whose salary is greater than ₹75,000.

# 4.   Generate a PDF report of the retrieved employees, including their names, roles, and salaries, formatted as a table.


import psycopg2
from fpdf import FPDF

# Database connection configuration
dbHost = "localhost"
dbName = "postgres"
dbUser = "postgres"
dbPassword = "********"
dbPort = 5432

# 1.
try:
    connection = psycopg2.connect(
        host=dbHost,
        database=dbName,
        user=dbUser,
        password=dbPassword,
        port=dbPort
    )
    cursor = connection.cursor()

    createTableQuery = """
        CREATE TABLE IF NOT EXISTS Employee (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL,
            salary NUMERIC NOT NULL
        );
    """
    cursor.execute(createTableQuery)
    connection.commit()

    print("Employee table created successfully.")
except Exception as error:
    print("Error while creating table:", error)

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")

# 2.
try:
    connection = psycopg2.connect(
        host=dbHost,
        database=dbName,
        user=dbUser,
        password=dbPassword,
        port=dbPort
    )
    cursor = connection.cursor()

    insertQuery = """
        INSERT INTO Employee (name, email, role, salary)
        VALUES (%s, %s, %s, %s);
    """

    employeeData = [
        ("John Doe", "john.doe@example.com", "Developer", 70000),
        ("Jane Smith", "jane.smith@example.com", "Manager", 85000),
        ("Michael Brown", "michael.brown@example.com", "Developer", 75000),
        ("Sara Lee", "sara.lee@example.com", "Manager", 90000),
        ("Tom Clark", "tom.clark@example.com", "Developer", 72000)
    ]

    cursor.executemany(insertQuery, employeeData)
    connection.commit()
    print(f"{cursor.rowcount} employee records inserted successfully.")
except Exception as error:
    print("Error inserting records:", error)
finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")

# 3.
try:
    connection = psycopg2.connect(
        host=dbHost,
        database=dbName,
        user=dbUser,
        password=dbPassword,
        port=dbPort
    )
    cursor = connection.cursor()

    selectQuery = """
        SELECT id, name, email, role, salary
        FROM Employee
        WHERE salary > 75000;
    """
    cursor.execute(selectQuery)
    records = cursor.fetchall()

    print("Employees with Salary greater than 75000:\n")
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Role: {row[3]}, Salary: {row[4]}")
except Exception as error:
    print("Error fetching data:", error)
finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("\nPostgreSQL connection closed.")

# 4.
try:
    connection = psycopg2.connect(
        host=dbHost,
        database=dbName,
        user=dbUser,
        password=dbPassword,
        port=dbPort
    )
    cursor = connection.cursor()
    selectQuery = """
        SELECT name, role, salary
        FROM Employee;
    """

    cursor.execute(selectQuery)
    records = cursor.fetchall()
    if not records:
        print("No employee records found.")
    else:
        pdf = FPDF()
        pdf.add_page()

        # Title
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'All Employee Details', ln=True, align='C')
        pdf.ln(5)

        # Table Header
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(60, 10, 'Name', border=1, align='C')
        pdf.cell(50, 10, 'Role', border=1, align='C')
        pdf.cell(40, 10, 'Salary', border=1, align='C')
        pdf.ln()

        # Table Rows
        pdf.set_font('Arial', '', 12)
        for row in records:
            name, role, salary = row
            pdf.cell(60, 10, name, border=1)
            pdf.cell(50, 10, role, border=1)
            pdf.cell(40, 10, str(salary), border=1)
            pdf.ln()

        # Save PDF
        outputFile = "all_employees_report.pdf"
        pdf.output(outputFile)
        print(f"PDF report generated: {outputFile}")
except Exception as error:
    print("Error generating report:", error)
finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed.")
