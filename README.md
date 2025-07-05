
# 📘 Student Marks Report Generator (Python PDF Project)

This project is a simple yet effective **Python automation tool** that reads student marks data from a CSV file and generates a **professionally formatted PDF report**. It includes a detailed table of marks, average statistics, and highlights the top and bottom performers.

---

## 📌 Features

- 📊 Auto-calculates **average, highest, and lowest marks**
- 🧾 Generates a clean, printable **PDF report**
- 📋 Data is stored in a CSV file for easy updates
- 🖨️ Includes formatted tables and headers
- 🖥️ Fully compatible with **VS Code** and **Google Colab**

---

## 📁 Repository Structure

```

student-marks-report/
│
├── data.csv                   # Sample student data (name, subject, marks)
├── student\_report\_generator.py # Python script to generate the report
├── output/
│   └── student\_marks\_report.pdf  # Auto-generated PDF report
├── requirements.txt           # Required Python libraries
└── README.md                  # Project overview (this file)

````

---

## 🚀 Getting Started

### 🔧 Prerequisites

Install Python and required libraries:

```bash
pip install pandas fpdf
````

### ▶️ Run the Script

```bash
python student_report_generator.py
```

The PDF will be saved in the `output/` folder.

---

## 📊 Sample Data (CSV)

```csv
Name,Subject,Marks
John Paul,Maths,85
Riya Sharma,Science,92
Amit Verma,English,78
...
```

You can modify this data in `data.csv` as needed.

---

## 📎 Output: Sample PDF Preview

The generated PDF includes:

* Project Title & Date
* Summary Statistics
* Formatted Marks Table
* Page Footer with numbers

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – data processing
* **FPDF** – PDF generation
* **VS Code** – development
* (Optional) Google Colab – to test online

---

## 📌 Author

👩‍💻 **Vidhi Mandhana**
Intern at Elite Tech Internships
GitHub: [github.com/VidhiMandhana](https://github.com/VidhiMandhana)

---

## 📜 License

This project is licensed under the MIT License.
Feel free to use and modify for learning or internal use!


