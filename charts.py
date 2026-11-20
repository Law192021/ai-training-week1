import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("employees.csv")
avg_salary = df.groupby("department")["salary"].mean()
avg_salary.plot(kind="bar")
plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
for i, value in enumerate(avg_salary):
    plt.text(i, value, f"{value:.0f}", ha="center")
plt.show()
plt.hist(df["salary"], bins=5, edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
for department, group in df.groupby("department"):
    plt.scatter(group["id"], group["salary"], label=department)
plt.title("ID vs Salary")
plt.xlabel("ID")
plt.ylabel("Salary")
plt.legend()
plt.show()
sales = [12, 15, 14, 18, 22, 25]
plt.plot(sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
