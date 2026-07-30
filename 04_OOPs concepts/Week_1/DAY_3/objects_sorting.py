#custom object sorting
class fruit:
    def __init__(self, name , amount):
        self.name=name
        self.amount=amount
    def __repr__(self):
        return f"{self.name} : {self.amount}"
    def sortitem(self):
        return sorted(all_fruits,key=lambda x:x.amount)
all_fruits=[fruit("apple",10),fruit("banana",5),fruit("orange",20)]
print(all_fruits)
print(fruit.sortitem(all_fruits))

#advance sorting but easy
class fruit:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def __repr__(self):
        return f"{self.name} : {self.amount}"
    def __lt__(self, other):
        return self.amount < other.amount
fruits = [fruit("apple", 10), fruit("banana", 5), fruit("orange", 20)]
print(fruits)
print(sorted(fruits))  # Sorts based on the __lt__ method