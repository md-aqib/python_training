import os
import re
import logging
from fpdf import FPDF

def is_log_file_exists(file_name='activity_logs.txt'):
    """Check if the log file exists."""
    try:
        if os.path.exists(file_name):
            print(f"File '{file_name}' exists.")
            return True
        else:
            print(f"File '{file_name}' does not exist.")
            return False
    except Exception as e:
        print(f"An error occurred while checking the file: {e}")
        return False

def extract_emails_from_file(file_name='activity_logs.txt'):
    """Extract and return list of emails found in the file."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
            emails = re.findall(email_pattern, content)
            return emails
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def unique_email_count(emails):
    """Count unique emails and log the count."""
    unique_emails = set(emails)
    count = len(unique_emails)
    logging.info(f"Unique email addresses found: {count}")
    print(f"Total unique email addresses: {count}")
    return unique_emails

def generate_pdf_report(emails, output_file='email_report.pdf'):
    """Generate a PDF report listing the emails and total count."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Email Extraction Report", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Total unique email addresses: {len(emails)}", ln=True)

    pdf.set_font("Arial", size=10)
    for email in emails:
        pdf.cell(0, 8, email, ln=True)

    pdf.output(output_file)
    print(f"PDF report '{output_file}' generated successfully.")

def main():
    logging.basicConfig(
        filename='email_log.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    file_name = 'activity_logs.txt'
    
    if not is_log_file_exists(file_name):
        return

    emails = extract_emails_from_file(file_name)
    if not emails:
        print("No valid email addresses found.")
        return

    unique_emails = unique_email_count(emails)
    generate_pdf_report(unique_emails)

if __name__ == "__main__":
    main()
