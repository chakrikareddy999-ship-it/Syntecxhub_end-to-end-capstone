# Week 4 Capstone Project
# Sales Data Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# Show first rows
print("First 5 Rows of Dataset")
print(df.head())

# Show column names
print("\nDataset Columns:")
print(df.columns)

# Dataset information
print("\nDataset Information")
print(df.info())

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# KPI Calculations
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_sales = df["Sales"].mean()
print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)
print("Average Sales:", avg_sales)

# Sales by Sub-Category
subcategory_sales = df.groupby("Sub-Category")["Sales"].sum()
plt.figure()
subcategory_sales.plot(kind="bar")
plt.title("Sales by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# Top 10 Sub-Categories
top_subcategories = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure()
top_subcategories.plot(kind="bar")
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Sales Distribution
plt.figure()
plt.hist(df["Sales"], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Correlation Heatmap
plt.figure()
sns.heatmap(df[["Sales", "Profit", "Quantity", "Discount"]].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()
print("\nProject Completed Successfully!")