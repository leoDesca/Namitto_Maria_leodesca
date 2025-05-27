#Exercise 
#submit your work on github for method overriding,method overloading and MRO 
#MRO method resolution order   two real world examples on the above concepts



# Real-world example 1: restuarant
from multipledispatch import dispatch

class Restaurant:
    def __init__(self, name):
        self.name = name
    def display_info(self):
        print(f"Welcome to {self.name}!")

    @dispatch(str)
    def make_order(self, dish):
        print(f"Order received: {dish}")

    @dispatch(list)
    def make_order(self, dishes):
        print("Order received:")
        for dish in dishes:
            print(f"-{dish}")

    @dispatch(dict)
    def make_order(self, order):
        print("Order received:")
        for dish, quantity in order.items():
            print(f"- {quantity}x {dish}")
restaurant = Restaurant("Leo's Place")
restaurant.display_info()

restaurant.make_order("Pasta ")
print()  

restaurant.make_order(["Margherita Pizza", "Salad", "rice Pudding"])
print()  
restaurant.make_order({"Spaghetti Bolognese": 2, "Garlic Bread": 3, "Wine": 2})

print()
print()





print()
# Real-world example 2: school
class School:
    def __init__(self, name):
        self.name = name
    
    @dispatch(str)
    def display_info(self, department):
        print(f"School Name: {self.name}, Department: {department}")
    @dispatch(str, int)
    def display_info(self, department, year):
        print(f"School Name: {self.name}, Department: {department}, Year: {year}")
school = School("Greenland High")
school.display_info("Computer Science") 
school.display_info("Computer Science", 2023)