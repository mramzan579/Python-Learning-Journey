# Numbers Analyzer
# Muhammad Ramzan
#   Analyzes multiple integers entered by the user.
#   Calculates total, average, max, min, even/odd counts,
#   sorted list, and unique numbers.
# ================

# Take multiple numbers as input from the user, separated by spaces
numbers = list(map(int, input("Enter multiple numbers separated by spaces: ").split()))

# Calculate basic statistics
total = sum(numbers)            # Sum of all numbers
average = total / len(numbers)  # Average of numbers
max_num = max(numbers)          # Maximum number
min_num = min(numbers)          # Minimum number
unique = set(numbers)           # Unique numbers (no duplicates)

# Separate even and odd numbers using list comprehensions
even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 != 0]

# Display results
print(f"Sorted Numbers: {sorted(numbers)}")          # Sorted list
print(f"Total: {total}")                             # Total sum
print(f"Average: {average:.2f}")                     # Average (2 decimal places)
print(f"Maximum: {max_num}")                         # Maximum number
print(f"Minimum: {min_num}")                         # Minimum number
print(f"Odd Numbers: {len(odd)}")                   # Count of odd numbers
print(f"Even Numbers: {len(even)}")                 # Count of even numbers
print(f"Unique Numbers: {sorted(unique)}")          # Sorted unique numbers
