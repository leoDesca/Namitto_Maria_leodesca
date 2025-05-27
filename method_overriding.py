

#real-world example 1: restaurant


class Restaurant:
    def __init__(self, name):
        self.name = name
    def make_order(self, dish):
        print(f"{self.name} has received your Order: 1x {dish}")
class FastFoodRestaurant(Restaurant):
    def make_order(self, dish):
        print(f"Order received: 2x {dish}. Your order will be ready in 10 minutes!")

restaurant = Restaurant("Leo's Place")
restaurant.make_order("Pasta")
fast_food_restaurant = FastFoodRestaurant("Bites")
fast_food_restaurant.make_order("Chickenburger")
print() 


print()
print()


#real-world example 2: school
class School:
    def __init__(self, name):
        self.name = name
    def display_info(self):
        print(f"School Name: {self.name}")
        print()
class ElementarySchool(School):
    def display_info(self):
        print(f"Elementary School Name: {self.name} - Welcome young learners!")
school2 = ElementarySchool("Sunnydale Elementary")
school2.display_info()