
class Restaurant:
    def make_order(self, dish):
        print(f"[{self.__class__.__name__}] Order received: 1x {dish}")

class FastFoodRestaurant(Restaurant):
    def make_order(self, dish):
        print(f"{self.__class__.__name__}:: Order received: 1x {dish}. Your order will be ready in 10 minutes!")


class FineDiningRestaurant(Restaurant):
    def make_order(self, dish):
        print(f"{self.__class__.__name__} :: Order received: 1x {dish}. Enjoy your meal in a luxurious setting!")

class SpecialtyRestaurant(FastFoodRestaurant, FineDiningRestaurant):
    pass


specialty_restaurant = SpecialtyRestaurant()


specialty_restaurant.make_order("The Explorer")
print()
    # Check the MRO of SpecialtyRestaurant
print("MRO of SpecialtyRestaurant:", SpecialtyRestaurant.__mro__)

print()

print()

print()

#real-world example 2: school

class BaseSchool:
    def display_info(self):
        print("BaseSchool: Displaying general school information.")
        
        
class ArtsSchool(BaseSchool):
    def display_info(self):
        print("ArtsSchool: Displaying arts school information.")
        
        
        
class ScienceSchool(BaseSchool):
    def display_info(self):
        print("ScienceSchool: Displaying science school information.")
        
        
class InterdisciplinarySchool(ArtsSchool, ScienceSchool):
    pass


interdisciplinary_school = InterdisciplinarySchool()

interdisciplinary_school.display_info()

print("MRO of InterdisciplinarySchool:", InterdisciplinarySchool.__mro__)