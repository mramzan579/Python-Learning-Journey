current_year = 2026

# CONCEPT: Base/Parent Class
# Single inheritance ki root class jo shared attributes (name, age) 
# aur basic utility methods (getAge) provide kar rahi hai.
class parrent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return current_year - self.age

    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge())


# CONCEPT: Derived/Child Class (Single Inheritance)
# 'child' class 'parrent' se inherit kar rahi hai. 
# super().__init__() ke zariye parent ke properties (name, age) reuse ho rahe hain 
# aur 'school' aapas mein specialized variable add ho raha hai.
class child(parrent):
    def __init__(self, name, age, school):
        super().__init__(name, age)  # Reusing parent constructor
        self.school = school

    # Method Overriding: Parent ke __str__ ko child requirement ke mutabiq enhance kiya gaya hai.
    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge()) + ' goes to {}'.format(self.school)


ali = child('Ali', 1990, 'joyland')
print(ali)


# CONCEPT: Base Class for Financial Calculation
# Core invoice class jo base amount handle karti hai.
class invoice:
    def __init__(self, customer_name, amount):
        self.customer_name = customer_name
        self.amount = amount

    def calculate_total(self):
        return self.amount


# CONCEPT: Method Overriding + super()
# 'vipinvoice' parent method ko override kar rahi hai.
# super().calculate_total() se pehle base price li jati hai, 
# phir us par discount percentage apply karke actual total banaya jata hai (DRY Principle).
class vipinvoice(invoice):
    def __init__(self, customer_name, amount, discount_percentage):
        super().__init__(customer_name, amount)  # Inherit parent attributes
        self.discount_percentage = discount_percentage

    def __str__(self):
        return f"Customer:{self.customer_name}, Amount: {self.amount}, discount:{self.discount_percentage}%"

    def calculate_total(self):
        total = super().calculate_total()  # Call parent method
        return total - (total * self.discount_percentage / 100)  # Apply math correction for percentage


inv1 = invoice('ali', 1000)
print(inv1.calculate_total())

inv1 = vipinvoice('ali', 1000, 10)
print(inv1.calculate_total())

# CONCEPT: Independent Parent Class 1
# Standalone class for handling camera features.
class camera:
    def __init__(self, resolution):
        self.resolution = resolution

    def record(self):
        return f"Recording at {self.resolution} resolution"


# CONCEPT: Independent Parent Class 2
# Standalone class for handling security alarm logic.
class alarm_system:
    def __init__(self, is_alarmed):
        self.is_alarmed = False

    def arm_system(self):
        self.is_alarmed = True
        return "Alarm system armed"

    def disarm_system(self):
        self.is_alarmed = False
        return "Alarm system disarmed"

    def trigger_alarm(self):
        if self.is_alarmed == True:
            return f"SIREN SOUNDING! ALARM TRIGGERED!"
        else:
            return "System is disarmed. No alarm."


# CONCEPT: Multiple Inheritance & Explicit Parent Init
# Class 'child' do alag parent classes (camera, alarm_system) se features inherit kar rahi hai.
# Dono parents ke __init__ methods ko explicitly call karke properly initialize kiya gaya hai.
class child(camera, alarm_system):
    def __init__(self, device_name, resolution):
        camera.__init__(self, resolution)     # Explicit call to parent 1 constructor
        alarm_system.__init__(self, False)    # Explicit call to parent 2 constructor
        self.device_name = device_name

    # Feature Integration: Combine behavior of both parent classes in one child method.
    def detect_motion(self):
        motion = self.record()        # Using Camera functionality
        status = self.trigger_alarm() # Using AlarmSystem functionality
        return f" [{self.device_name}] {motion} | {status}"


device1 = child("SecurityCam", "1080p")
print(device1.detect_motion())

#multilevel inheritance example(order processing system)
# Level 1: Base Class (Parent)
# Base class jo core order data aur primary price structure define karti hai.
class base_order:
    def __init__(self, order_id, base_price):
        self.order_id = order_id
        self.base_price = base_price

    def get_total(self):
        return self.base_price

# Level 2: Child Class (Inherits from base_order)
# Tax logic add karti hai aur super().get_total() se base price fetch karti hai.
class taxed_order(base_order):
    def __init__(self, order_id, base_price, tax_rate):
        super().__init__(order_id, base_price)  # Pass base data to Level 1
        self.tax_rate = tax_rate

    def get_total(self):
        tax_amount = self.base_price * self.tax_rate / 100
        final = super().get_total() + tax_amount  # Base Price + Tax
        return final
# Level 3: Grandchild Class (Inherits from taxed_order)
# Discount apply karti hai. super().get_total() pehle Level 2 se taxed amount laata hai.
class discounted_taxed_order(taxed_order):
    def __init__(self, order_id, base_price, tax_rate, discount_amount):
        super().__init__(order_id, base_price, tax_rate)  # Pass data to Level 2
        self.discount_amount = discount_amount

    def get_total(self):
        discounted = super().get_total() - self.discount_amount  # (Base + Tax) - Discount
        return discounted

emp1 = base_order(101, 500)
print(f"Base Order Total: {emp1.get_total()}")  # Output: 500

emp2 = taxed_order(102, 500, 10)
print(f"Taxed Order Total: {emp2.get_total()}")  # Output: 550.0

emp3 = discounted_taxed_order(103, 500, 10, 50)
print(f"Discounted Taxed Order Total: {emp3.get_total()}")  # Output: 500.0

#hierarchical inheritance example(employee payroll system)
# Base Class: employee
class employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
# Method to calculate salary for base employee
    def calculate_salary(self):
        return self.base_salary
# Derived Class: developer inherits from employee
class developer(employee):
    def __init__(self, emp_id, name, base_salary, bonus):
        super().__init__(emp_id, name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus
# Derived Class: manager inherits from employee
class manager(employee):
    def __init__(self, emp_id, name, base_salary, allowance):
        employee.__init__(self, emp_id, name, base_salary)
        self.allowance = allowance
    def calculate_salary(self):
        return employee.calculate_salary(self) + self.allowance
#testing the classes
ali=employee(1,"ali",50000)
print(f"Employee Salary: {ali.calculate_salary()}")  # Output: 50000
ahmed=developer(2,"ahmed",60000,10000)
print(f"developer salary: {ahmed.calculate_salary()}")  # Output: 70000
sara=manager(3,"sara",70000,15000)
print(f"Manager Salary: {sara.calculate_salary()}")  # Output: 85000

#hybrid inheritance example(Gaming Character Abilities)
# Base Class: character
class character:
    def __init__(self, name):
        self.name = name
class warrior(character):
    def __init__(self,name):
        super().__init__(name)
    # Method to simulate an attack action for the warrior class
    def attack(self):
        return f"{self.name} attacks the sword."
# Derived Class: mage inherits from character
class mage(character):
    def __init__(self,name):
        super().__init__(name)
    def cast_spell(self):
        return f"{self.name} casts a fireball."
# Derived Class: paladin inherits from both warrior and mage (Multiple Inheritance)
class paladin(warrior,mage):
    def __init__(self,name):
        super().__init__(name)
    # Method to combine abilities from both parent classes (warrior and mage)
    def ultimate_move(self):
        return f"{self.name} perofrmed tasks like : {self.attack()} and {self.cast_spell()}"
#testing the paladin class
ali=paladin("ali")
print(ali.ultimate_move())