"""
Create four Matplotlib charts from employees.csv.
Place employees.csv beside this script, then run:
    python create_charts.py
The PNG files are saved beside the script.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "employees.csv"
OUTPUT_DIR = HERE

employees = pd.read_csv(CSV_PATH)

required = {"id", "department", "salary"}
missing = required - set(employees.columns)
if missing:
    raise ValueError(f"employees.csv is missing required columns: {', '.join(sorted(missing))}")

# 1. Average salary by department
average_salary = employees.groupby("department")["salary"].mean().sort_index()
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(average_salary.index, average_salary.values, color="#4C78A8")
ax.set_title("Average Salary by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")
ax.bar_label(bars, fmt="%.0f", padding=3)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "average_salary_by_department.png", dpi=150)
plt.close(fig)

# 2. Salary histogram with exactly 5 bins
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(employees["salary"], bins=5, color="#59A14F", edgecolor="white")
ax.set_title("Distribution of Employee Salaries")
ax.set_xlabel("Salary")
ax.set_ylabel("Number of Employees")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "salary_histogram.png", dpi=150)
plt.close(fig)

# 3. Employee ID vs salary, coloured by department
fig, ax = plt.subplots(figsize=(8, 5))
for department, group in employees.groupby("department"):
    ax.scatter(group["id"], group["salary"], label=department, s=65, alpha=0.85)
ax.set_title("Employee ID vs Salary by Department")
ax.set_xlabel("Employee ID")
ax.set_ylabel("Salary")
ax.legend(title="Department")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "id_vs_salary_scatter.png", dpi=150)
plt.close(fig)

# 4. Monthly sales, January through June
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(months, sales, marker="o", linewidth=2, color="#E15759")
ax.set_title("Monthly Sales (Jan–Jun)")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.set_ylim(0, max(sales) + 5)
ax.grid(True, axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "monthly_sales_line.png", dpi=150)
plt.close(fig)

print(f"Created four charts in {OUTPUT_DIR}")
