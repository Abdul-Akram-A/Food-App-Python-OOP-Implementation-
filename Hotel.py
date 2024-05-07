from Abstract import Abstract
from FoodMenu import Menus
class Hotels(Abstract):
    def __init__(self,name,rating,location):
        super().__init__(name,rating)
        self.location = location
        self.__FoodMenu=[]
        
    # Getter and Setter for the food items
    @property
    def FoodMenu(self):
        return self.__FoodMenu
    
    @FoodMenu.setter
    def FoodMenu(self,menuList):
        for menu in menuList:
            if not isinstance(menu,Menus):
                print("Invalid food menu")
                return
        self.__FoodMenu=menuList
        