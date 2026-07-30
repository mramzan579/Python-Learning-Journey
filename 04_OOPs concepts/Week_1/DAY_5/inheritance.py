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