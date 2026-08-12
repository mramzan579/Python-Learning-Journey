#Duck Typing Payment System
class creditCard:
    def __init__(self, card_number):
        self.__card_number=card_number
    def pay(self, amount):
        print(f"{amount} paid through credit card using card number {self.__card_number}")
class cryptoWallet:
    def __init__(self, card_number):
        self.__card_number=card_number
    def pay(self, amount):
        print(f"{amount} Paid through cryptoWallet using wallet number {self.__card_number}")
class EasyPaisa:
    def __init__(self, card_number):
        self.__card_number=card_number
    def pay(self, amount):
        print(f"{amount} paid through easypaisa account using account number {self.__card_number}.")
def make_payment(payment_method, amount):
    payment_method.pay(amount)
first_payment=creditCard(1000)
second_payment=cryptoWallet(9878)
third_payment=EasyPaisa(5437)
make_payment(third_payment,10000)

#challenge 2: Duck Typing for different types of shapes
class shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
class reactangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
class triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return self.base+self.height+((self.base**2+self.height**2)**0.5)
def print_shape_info(shape_obj):
    print(f"Area: {shape_obj.area()}")
    print(f"Perimeter: {shape_obj.perimeter()}")
tr=triangle(3,4)
rec=reactangle(5,6)
cir=circle(7)
print_shape_info(tr)
print_shape_info(rec)
print_shape_info(cir)

#Challenge 3: Operator Overloading for a money class
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def __str__(self):
        return f"{self.amount} {self.currency}"
    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            raise ValueError("Cannot add amounts with different currencies.")
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
m1=Money(100, "USD")
m2=Money(200, "USD")
m3=Money(100, "EUR")
# Adding two Money objects with the same currency
result = m1 + m2
print(f"Result of addition: {result}")  # Output: 300 USD

# Attempting to add Money objects with different currencies
try:
    result = m1 + m3
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Cannot add amounts with different currencies.
print(m1==m3)

#challenge 4: multiformat data export
class JSONexporter:
    def export(self, data):
        print(f"Exporting data in JSON format: {data}")
class CSVexporter:
    def export(self, data):
        print(f"Exporting data in CSV format:\n {','.join(data.keys())}\n{','.join(map(str, data.values()))}")
class XMLexporter:
    def export(self, data):
        xml_data = "<data>\n"
        for key, value in data.items():
            xml_data += f"  <{key}>{value}</{key}>\n"
        xml_data += "</data>"
        print(f"Exporting data in XML format:\n{xml_data}")
def report_from_each(exporter, data):
    exporter.export(data)
data = {"name": "John Doe", "age": 30, "city": "New York"}
json_exporter = JSONexporter()
csv_exporter = CSVexporter()
xml_exporter = XMLexporter()

report_from_each(json_exporter, data)
report_from_each(csv_exporter, data)
report_from_each(xml_exporter, data)

#challenge middleware pipeline
class LoggingMiddleware:
    def process(self, request):
        print(f"Logging request: {request}")
class AuthMiddleware:
    def process(self, request):
        print(f"Authenticating request: {request}")
class RateLimitingMiddleware:
    def process(self, request):
        print(f"Rate limiting request: {request}")
def run_pipeline(middlewares, request):
    for middleware in middlewares:
        middleware.process(request)
requests={"path":"/api/data","method":"GET", "token":"abc123"}
middlewares=[LoggingMiddleware(),AuthMiddleware(),RateLimitingMiddleware()]
run_pipeline(middlewares,requests)