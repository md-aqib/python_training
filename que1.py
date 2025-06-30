# Click the link to download activity_logs.txt

# Log Analysis and Reporting

# Scenario: Your company’s system generates daily log files with user activity.

# Write a Python program to:

# 1.   Check if a file named activity_logs.txt exists; if not, handle the exception gracefully.

# 2.   Read the file and use regular expressions to extract all valid email addresses.

# 3.   Count the unique email addresses and log the count using Python’s logging module.

# 4.   Generate a PDF report summarizing the extracted email addresses and their total count.


import os
import re
import logging
from fpdf import FPDF

# 1.
def isLogFileExists():
    fileName = 'activity_logs.txt'
    try:
        if os.path.exists(fileName):
            print(f"File '{fileName}' exists.")
        else:
            print(f"File '{fileName}' does not exist.")
    except Exception as e:
        print(f"An error occurred while checking the file: {e}")
isLogFileExists()

# 2.
def extractEmailsFromFile(fileName='activity_logs.txt'):
    try:
        # we can use manually open(), close() function, but with automatically closes the file even after getting exception
        with open(fileName, 'r') as file:
            content = file.read()
            # Regular expression pattern for matching email addresses
            emailPattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
            emails = re.findall(emailPattern, content)
            
            if emails:
                print("Valid email addresses found:")
                for email in emails:
                    print(email)
                return emails
            else:
                print("No valid email addresses found.")
    except FileNotFoundError:
        print(f"File '{fileName}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
extractEmailsFromFile()

# 3.
logging.basicConfig(
    filename='email_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def uniqueEmailCount(emails):
    try:
        # Get unique emails
        uniqueEmails = set(emails)
        count = len(uniqueEmails)

        logging.info(f"Unique email addresses found: {count}")
        print(f"Total unique email addresses: {count}")
    except FileNotFoundError:
        logging.error(f"File '{fileName}' not found.")
        print(f"File '{fileName}' does not exist.")
    except Exception as e:
        logging.exception("An error occurred while processing the file.")
        print(f"An error occurred: {e}")
uniqueEmailCount(extractEmailsFromFile())

# 4.
def generatePdf(emails, outputFile='email_report.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Email Extraction Report", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Total unique email addresses: {len(emails)}", ln=True)

    pdf.set_font("Arial", size=10)
    for email in emails:
        pdf.cell(0, 8, email, ln=True)

    pdf.output(outputFile)
    print(f"PDF report '{outputFile}' generated.")
generatePdf(extractEmailsFromFile())


