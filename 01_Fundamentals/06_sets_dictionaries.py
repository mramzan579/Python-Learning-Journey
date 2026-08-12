# Word meanings dictionary
word_meanings = {
    "table": "a piece of furniture",
    "cat": "a small pet animal",
    "facts": "sun sets in the west. sun rises in the east.",
    "computer": "Electronic machine processes raw data",
    "capacitor": "Linear and passive storage element"
}

print(f"Available words: {list(word_meanings.keys())}")
word = input("Enter a word: ").lower()
meaning = word_meanings.get(word)

if meaning:
    print(f"Meaning: {meaning}")
else:
    print("Word not found.")

# Classrooms needed (Set handles uniqueness)
subjects = {"Python", "Java", "C++", "Python", "Javascript", "Java", "Python", "Java", "C++", "C"}
print(f"Total classrooms needed: {len(subjects)}")

# Dictionary population
subject_marks = {
    "phy": input("Enter phy marks: "),
    "chem": input("Enter chem marks: "),
    "bio": input("Enter bio marks: ")
}
print(subject_marks)

# Demonstrating set behavior with distinct types
val_set = {9, "9.0"} 
print(f"Set contents: {val_set}")