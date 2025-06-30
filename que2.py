# Click the link to download the dataset sales_data.csv

# File Handling and Data Analysis

# Scenario: A dataset file sales_data.csv contains monthly sales figures for a company.

# Write a Python program to:

# 1.   Read the file using Pandas and calculate the following:

# Total sales.
# Average monthly sales.
# 2.   Write the results into a PDF report with a short analysis summary.


import pandas as pd
from fpdf import FPDF

# 1.
def calculateSalesSummary(filePath):
    salesData = pd.read_csv(filePath)
    totalSales = salesData['Sales'].sum()
    averageMonthlySales = salesData['Sales'].mean()
    
    print(f"Total Sales: ${totalSales}")
    print(f"Average Monthly Sales: ${averageMonthlySales}")
    
    return totalSales, averageMonthlySales

# 2.
def generatePdf(totalSales, averageMonthlySales):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Monthly Sales Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Total Sales: ${totalSales}", ln=True)
    pdf.cell(0, 10, f"Average Monthly Sales: ${averageMonthlySales}", ln=True)
    pdf.ln(10)

    pdf.multi_cell(0, 10,
        "Analysis Summary:\n"
        "This report shows the total and average monthly sales.\n"
        "These numbers help us understand how the company is performing over time.\n"
        "Stable or increasing averages suggest good performance."
    )
    pdf.output("sales_report.pdf")
    print("PDF report saved as 'sales_report.pdf'.")

filePath = 'sales_data.csv'
totalSales, averageMonthlySales = calculateSalesSummary(filePath)
generatePdf(totalSales, averageMonthlySales)

