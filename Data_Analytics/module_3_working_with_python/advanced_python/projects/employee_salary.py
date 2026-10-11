import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from openpyxl.drawing.image import Image
import pandas as pd

# 1. Generate synthetic data using NumPy
np.random.seed(42)  # For reproducible random data
n_employees = 10

emp_ids = range(101, 101 + n_employees)
names = [
    'Alice Smith',
    'Bob Jones',
    'Charlie Brown',
    'Diana Prince',
    'Evan Wright',
    'Fiona Gallagher',
    'George Clark',
    'Hannah Abbott',
    'Ian Malcolm',
    'Julia Roberts',
]
departments = np.random.choice(
    ['Engineering', 'Marketing', 'HR', 'Finance'], size=n_employees
)
basic_salary = np.random.randint(40000, 95000, size=n_employees)
allowances = np.round(basic_salary * 0.12, 2)  # 12% of basic
deductions = np.round(basic_salary * 0.05, 2)  # 5% of basic

# 2. Structure data in a Pandas DataFrame & calculate Net Salary
df = pd.DataFrame(
    {
        'Emp ID': emp_ids,
        'Name': names,
        'Department': departments,
        'Basic Salary': basic_salary,
        'Allowances': allowances,
        'Deductions': deductions,
    }
)

df['Net Salary'] = df['Basic Salary'] + df['Allowances'] - df['Deductions']

# 3. Create a Matplotlib chart (Department-wise Average Net Salary)
dept_salary = df.groupby('Department')['Net Salary'].mean()

plt.figure(figsize=(6, 4))
dept_salary.plot(kind='bar', color='#4A90E2', edgecolor='black')
plt.title('Average Net Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Net Salary')
plt.xticks(rotation=30)
plt.tight_layout()

chart_path = 'salary_chart.png'
plt.savefig(chart_path, dpi=150)
plt.close()

# 4. Export DataFrame to Excel
file_name = 'employee_salary_analytics.xlsx'
df.to_excel(file_name, index=False, sheet_name='Salary Data')

# 5. Use Openpyxl to embed the Matplotlib chart into the spreadsheet
wb = openpyxl.load_workbook(file_name)
ws = wb['Salary Data']

# Load image and position it next to the table
img = Image(chart_path)
ws.add_image(img, 'I2')  # Places the chart starting at cell I2

wb.save(file_name)
print(f"Success! Advanced Excel file saved as '{file_name}'.")