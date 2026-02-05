# ⚡ Weekly Energy Consumption Tracker

## 📝 Description
This tool is designed to track and analyze household or laboratory energy consumption over a 7-day period. It takes daily unit consumption as input and provides a detailed statistical summary, including total cost estimation.

This project serves as an exercise in handling multiple data points (lists) and performing aggregate calculations without using loops.

## ✨ Features
 **Batch Input Handling:** Processes 7 days of data in a single input line using string splitting.
 **Strict Validation:** * Ensures exactly 7 data points are provided.
    * Prevents negative unit values, as energy consumption cannot be less than zero.
 **Statistical Insights:** Automatically calculates the Total, Maximum, Minimum, and Average units consumed.
 **Cost Estimation:** Calculates the total weekly bill based on a fixed unit price ($11.35).

## 🛠️ Programming Concepts Used
 **List Comprehension:** For efficient conversion of string inputs into a list of integers.
 **Aggregates:** Utilizing `sum()`, `max()`, and `min()` for quick data analysis.
 **Error Handling:** Conditional logic (`if-elif-else`) to validate data integrity.
 **String Manipulation:** Using `.split()` to parse user input.

## ⚠️ Known Limitations
 **Beginner-Level Logic:** The tool assumes a fixed unit price and does not account for tax or slab-based billing used in actual utility bills.
 **Data Persistence:** Calculations are performed in-memory and are not saved to a database or file.
 **Input Sensitivity:** The program will fail if non-numeric characters (like letters) are entered.

*Status: Completed as a practical data-handling exercise.*