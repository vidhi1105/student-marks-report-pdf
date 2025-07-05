import pandas as pd
from fpdf import FPDF
from datetime import datetime
import os

# ✅ Create output folder if not exists
os.makedirs("output", exist_ok=True)

# ✅ Sample data
data = {
    "Name": [
        "John Paul", "Riya Sharma", "Amit Verma", "Sneha Mehta",
        "David R.", "Pooja Patil", "Rakesh Nair", "Anjali Singh",
        "Vikram Rana", "Neha Kulkarni"
    ],
    "Subject": [
        "Maths", "Science", "English", "History",
        "Maths", "Science", "English", "History",
        "Computer", "Biology"
    ],
    "Marks": [85, 92, 78, 88, 74, 91, 67, 81, 89, 94]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

# ✅ Summary Stats
avg_marks = df["Marks"].mean()
highest = df.loc[df["Marks"].idxmax()]
lowest = df.loc[df["Marks"].idxmin()]
report_date = datetime.now().strftime("%d %B %Y")

# ✅ PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, "Student Marks Report", ln=True, align='C')
        self.set_font("Arial", '', 12)
        self.cell(0, 10, f"Report Date: {report_date}", ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

# ✅ Generate PDF
pdf = PDF()
pdf.add_page()

# 📌 Summary Section
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Summary Statistics:", ln=True)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"Average Marks: {avg_marks:.2f}", ln=True)
pdf.cell(0, 10, f"Highest: {highest['Name']} ({highest['Subject']}) - {highest['Marks']} marks", ln=True)
pdf.cell(0, 10, f"Lowest: {lowest['Name']} ({lowest['Subject']}) - {lowest['Marks']} marks", ln=True)
pdf.ln(10)

# 📋 Table Header
pdf.set_font("Arial", 'B', 12)
pdf.set_fill_color(200, 220, 255)
pdf.cell(70, 10, "Name", border=1, fill=True, align='C')
pdf.cell(60, 10, "Subject", border=1, fill=True, align='C')
pdf.cell(30, 10, "Marks", border=1, fill=True, align='C')
pdf.ln()

# 📋 Table Rows
pdf.set_font("Arial", '', 12)
for _, row in df.iterrows():
    pdf.cell(70, 10, row["Name"], border=1)
    pdf.cell(60, 10, row["Subject"], border=1)
    pdf.cell(30, 10, str(row["Marks"]), border=1, align='C')
    pdf.ln()

# 💾 Save PDF
pdf.output("output/student_marks_report.pdf")
print("✅ PDF successfully saved to output/student_marks_report.pdf")
