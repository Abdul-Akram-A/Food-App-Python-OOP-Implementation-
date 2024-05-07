from FoodItems import FoodItem
from FoodMenu import Menus
from Hotel import Hotels
class FoodManager:
    def __init__(self):
        self.Hotels=self.__PrepareHotesl()
        
    def __PrepareFoodItem(self):
        
        item1=FoodItem("Beef_Briyani",4.5,200,"Very Meaty")
        item2=FoodItem("Veg_Briyani",3.7,130,"Subtle")
        item3=FoodItem("Noodles",4.0,110,"Yummy!")
        item4=FoodItem("Parota",3.9,40,"Chewy")
        item5=FoodItem("Naan",3,40,"Rough")
        return [item1,item2,item3,item4,item5]
    def __PrepareFoodMenu(self):
        FoodItems=self.__PrepareFoodItem()
        Menu1=Menus("Veg")
        Menu1.FoodItems=[FoodItems[1],FoodItems[4]]
        Menu2=Menus("Non-Veg")
        Menu2.FoodItems=[FoodItems[0],FoodItems[3]]
        Menu3=Menus("Chinnes")
        Menu3.FoodItems=[FoodItems[2]]
        return[Menu1,Menu2,Menu3]
    def __PrepareHotesl(self):
        FoodMenu=self.__PrepareFoodMenu()
        Hotel1 = Hotels("Taj",5.0,"Mumbai")
        Hotel1.FoodMenu=[FoodMenu[0],FoodMenu[1]]
        Hotel2 = Hotels("Al",4.9,"Dubai")
        Hotel2.FoodMenu=[FoodMenu[1],FoodMenu[2]]
        Hotel3 = Hotels("The Leela", 4.8, "Delhi")
        Hotel3.FoodMenu=[FoodMenu[0],FoodMenu[1],FoodMenu[2]]
        return [Hotel1,Hotel2,Hotel3]
    def Find_Hotel(self,name):
        for hotel in self.Hotels:
            if hotel.name == name:
                return hotel
        print("No such Hotel is available.")