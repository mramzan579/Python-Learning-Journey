# 📊 Student Marks Analyser

## 📝 Description
This is a basic data-processing tool designed to automate the calculation of total marks, percentages, and grade assignments for a student. It serves as a practical exercise in handling user input, performing arithmetic operations, and implementing multi-level conditional logic.

## ✨ Features
 **Data Validation:** Uses a logical check to ensure all input marks fall within the valid range of 0 to 100.
 **Automated Grading:** Assigns a letter grade (A, B, C, D, or Fail) based on the calculated percentage.
 **List Integration:** Stores subject marks in a list to utilize Python's built-in `sum()` and `len()` functions for efficient calculation.
 **Clean Output:** Displays a formatted summary of the total marks, percentage, and final grade.

## 🛠️ Programming Concepts Used
 **Input Validation:** Implementing a range-check logic to handle incorrect data entry.
 **Built-in Functions:** Using `sum()` for addition and `any()` for efficient conditional checking across multiple variables.
 **Comparison Operators:** Utilizing `>=`, `<`, and `>` to determine grade boundaries.
 **F-Strings:** For dynamic and readable output formatting.

## ⚠️ Known Limitations
 This tool is a **logic-building exercise**; it is not designed for professional scale as it handles a fixed number of subjects (5).
 It does not currently use loops for input, meaning each subject must be entered individually.
 Basic error handling: It will crash if a non-numeric value (e.g., text) is entered.

*Status: Completed as a logic-building challenge during my Python Journey.*