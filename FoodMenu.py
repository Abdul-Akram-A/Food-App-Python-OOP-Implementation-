
from Abstract import Abstract
from FoodItems import FoodItem

class Menus(Abstract):
    def __init__(self,name):
        super().__init__(name)
        self.__FoodItems = []
        
    # Getter and Setter for the food items
    @property
    def FoodItems(self):
        return self.__FoodItems
    
    @FoodItems.setter
    def FoodItems(self,foods):
        for food in foods:
            if not isinstance(food,FoodItem):
                print("Invalid food items")
                return True
        self.__FoodItems=foods
    