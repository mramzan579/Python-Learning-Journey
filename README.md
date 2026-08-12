```markdown
# 🚀 Python & Backend Engineering Journey

Welcome to my comprehensive Python and Backend Engineering repository. This repo documents a hands-on, progressive learning roadmap covering core Python computational logic, utility script architecture, exception-safe file handling, production-ready Object-Oriented Programming (OOP) designs, and modern asynchronous FastAPI backend engineering.

---

## 📂 Repository Structure

```text
PYTHON-LEARNING-JOURNEY/
│
├── 01_Fundamentals/          # Core syntax, logic, data structures & recursion
│   ├── 01_variables_conditions.py
│   ├── 02_lists_tuples.py
│   ├── 03_for_loops_exercises.py
│   ├── 003_while_for_loops.py
│   ├── 04_functions.py
│   ├── 05_recursive_functions.py
│   └── 06_sets_dictionaries.py
│
├── 02_Basic_Tools/           # Algorithmic utility scripts & mini CLI projects
│   ├── number_analyzer/
│   ├── number_system_conversion/
│   ├── ohms_law_calculator/
│   ├── student_result_system/
│   ├── students_marks_analyser/
│   └── weekly_energy_tracker/
│
├── 03_file_handling/         # File I/O stream operations & error handling
│   ├── 01_file_modes.py
│   ├── 02_try_except.py
│   └── 03_the_final_problem.py
│
├── 04_OOPs concepts/         # Complete OOP Suite (4 Pillars + Design Patterns)
│   ├── 01_classes_objects.py
│   ├── 02_more_about_objects.py
│   ├── 03_objects_sorting.py
│   ├── 04_challenges.py
│   ├── 05_inheritance.py
│   ├── 06_decorators.py
│   ├── 08_abstraction.py
│   ├── 09_encapsulation.py
│   └── 10_polymorphism.py
│
└── 05_FastAPI_Backend/       # Asynchronous RESTful APIs, Pydantic & Middleware  (Upcoming)
    └── main.py

```

---

## 📚 Comprehensive Module Deep Dives

---

### Module 1: Python Core Fundamentals (`01_Fundamentals/`)

This module establishes core programming concepts, memory behavior, and algorithmic thinking in Python.

* **Variables & Control Flow (`01_variables_conditions.py`):**
* Data typing, dynamic binding, and conditional branching (`if-elif-else`).


* **Sequence Data Structures (`02_lists_tuples.py`):**
* List indexing, slicing, mutability vs immutability safety, and tuple unpacking.


* **Iterative Loops (`03_for_loops_exercises.py`, `003_while_for_loops.py`):**
* Algorithmic execution using `range()`, nested loops, indefinite `while` iteration, and loop control statements (`break`, `continue`).


* **Functional Programming (`04_functions.py`):**
* Modular code execution, positional vs keyword arguments, dynamic parameters (`*args`, `**kwargs`), and variable scopes (`local` vs `global`).


* **Call Stack Recursion (`05_recursive_functions.py`):**
* Solving self-referential problems using explicit base cases to prevent stack overflow errors (`RecursionError`).


* **Mapped & Set Collections (`06_sets_dictionaries.py`):**
* O(1) lookup operations using Hash Maps (`Dictionaries`), set operations (`union`, `intersection`), and dictionary comprehensions.



---

### Module 2: Applied Utility Tools (`02_Basic_Tools/`)

A collection of standalone, domain-specific computational scripts built using foundational Python concepts:

* **Number Analyzer & System Converters:** Mathematical number property evaluations and base conversions (Binary, Decimal, Hexadecimal).
* **Engineering Tools (Ohm's Law Calculator):** Voltage, current, and resistance calculations with input validation.
* **Data Processing Scripts:** Student marks analyzers, result generation systems, and weekly energy consumption tracking.

---

### Module 3: File Handling & Exception Safety (`03_file_handling/`)

Focuses on persistent storage operations, stream handling, and writing fault-tolerant Python applications.

* **File Streams & Modes (`01_file_modes.py`):**
* Managing file descriptors using standard context managers (`with open()`) across read (`r`), write (`w`), and append (`a`) modes.


* **Defensive Error Handling (`02_try_except.py`):**
* Handling runtime failures safely using `try-except-else-finally` blocks and raising domain-specific exceptions.


* **Data Transformation (`03_the_final_problem.py`):**
* Processing CSV streams, parsing structured data, performing runtime updates, and writing modified state back to storage.



---

### Module 4: Object-Oriented Programming Suite (`04_OOPs concepts/`)

A comprehensive mastery suite covering object models, advanced functional decorators, and the 4 Core Pillars of Object-Oriented Programming.

#### Key Architectural Concepts:

* **Classes & State (`01_classes_objects.py`, `02_more_about_objects.py`):**
* Blueprint design, constructors (`__init__`), instance variables vs class variables, and dynamic state modification.


* **Object Collections & Sorting (`03_objects_sorting.py`):**
* Sorting custom object structures using `lambda` keys and `operator.attrgetter`.


* **Inheritance & Hierarchy (`05_inheritance.py`):**
* Reusing structure via single, multiple, and multilevel inheritance while maintaining method resolution order with `super()`.


* **Python Decorators (`06_decorators.py`):**
* Higher-order wrapper functions for performance benchmarking, call logging, and authorization checks.



---

#### 🏛 The 4 Pillars of OOP

#### 1. Abstraction (`08_abstraction.py`)

Enforces uniform architectural contracts by hiding internal implementation details behind abstract interfaces using Python's `abc.ABC` module and `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def generate_response(self, prompt: str):
        pass

    @abstractmethod
    def get_token_count(self, text: str):
        pass

```

#### 2. Encapsulation (`09_encapsulation.py`)

Protects object state from external manipulation via double-underscore private attributes (`__variable`) and provides controlled access through Pythonic `@property` getters and setters.

```python
class Patient:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature  # Triggers property setter

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if 35.0 <= value <= 42.0:
            self.__temperature = value
        else:
            raise ValueError("Invalid human body temperature!")

```

#### 3. Inheritance (`05_inheritance.py`)

Facilitates hierarchical code reuse and extension across base and derived classes using `super()`.

#### 4. Polymorphism (`10_polymorphism.py`)

Provides dynamic method execution across varied data types through:

* **Duck Typing:** Behavior-driven interface handling (*"If it walks like a duck..."*).
* **Method Overriding:** Redefining parent class behaviors within child instances.
* **Operator Overloading:** Customizing standard operator behavior (`+`, `==`) via special dunder methods (`__add__`, `__eq__`).
* **Middleware Pipelines:** Processing request payloads sequentially through polymorphic middleware execution steps.

---

### Module 5: FastAPI Backend Engineering (`05_FastAPI_Backend/`)

Modern asynchronous web API development focused on high-performance backend systems:

* **RESTful API Routes:** Path parameters, query parameters, and JSON response bodies.
* **Data Validation:** Pydantic models, request validation, and automatic OpenAPI schema generation.
* **Dependency Injection:** Modular service layers, authorization middlewares, and database sessions.
* **Asynchronous Execution:** High-concurrency route handlers using `async`/`await`.

---

## 🛠 Running the Project

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/PYTHON-LEARNING-JOURNEY.git](https://github.com/your-username/PYTHON-LEARNING-JOURNEY.git)
cd PYTHON-LEARNING-JOURNEY

```


2. **Execute any module script:**
```bash
python "04_OOPs concepts/10_polymorphism.py"

```


3. **Run FastAPI Backend:**
```bash
pip install fastapi uvicorn
uvicorn 05_FastAPI_Backend.main:app --reload

```



```

```
