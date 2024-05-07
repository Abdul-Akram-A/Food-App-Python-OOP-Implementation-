from FoodManager import FoodManager

class Mainmenu:
    __Options={1:"Show_Hotels",2:"Show_FoodItems",3:"Search_Hotels",4:"Show_FoodMenu",5:"Back"}
    def __init__(self):
        self.__FoodManager=FoodManager()
    def ShowHotels(self):
        for h in self.__FoodManager.Hotels:
            print(f"{h.name}=>{h.rating}")
    def ShowFoodItems(self,foodItems=None):
        hotel_names=[hotel.name for hotel in self.__FoodManager.Hotels]
        if foodItems is None:
            choice_h=input("Select which Hotel:")
            if choice_h in hotel_names:
                for hotel in self.__FoodManager.Hotels:
                    if hotel.name == choice_h:
                        print(f"Hotel: {hotel.name}")
                        for menu in hotel.FoodMenu:
                            print(f"Menu: {menu.name}")
                            for food in menu.FoodItems:
                                print(f"Food: {food.name}, Rating: {food.rating}, Description: {food.description}")
            else:
                print("Invalid Choice!")
        else:
            
            for hotel in self.__FoodManager.Hotels:
                if hotel.name == foodItems:
                    print(f"Hotel: {hotel.name}")
                    for menu in hotel.FoodMenu:
                        print(f"Menu: {menu.name}")
                        for food in menu.FoodItems:
                            print(f"Food: {food.name}, Rating: {food.rating}, Description: {food.description}")
                            
    
        
    def SearchHotels(self):
        Hotel_name=input("Enter Hotel Name:")
        res=self.__FoodManager.Find_Hotel(Hotel_name)
        if res is not None:
            print(f"{Hotel_name} is available")
            # print(res.name)
            self.ShowFoodItems(res.name)
    def ShowFoodMenu(self):
        hotel_names=[hotel.name for hotel in self.__FoodManager.Hotels]
        choice=input("Enter Hotel Name:")
        print("Available Menus:")
        if choice in hotel_names:
            for hotel in self.__FoodManager.Hotels:
                if choice == hotel.name:
                    for menu in hotel.FoodMenu:
                        print(menu.name)
        else:
            print("Invalid Choice")
                
    def Back(self):
        from Main import Initialization
        Init=Initialization()
        Init.Init()

    def Start(self):
        while True:
            for keys,values in self.__Options.items():
                print(f"{keys}.{values}",end=" ")
            print()
            try:
                choice=int(input("Enter your choice:"))
                value=self.__Options[choice].replace("_","")
                getattr(self,value)()
            except (ValueError,KeyError):
                print("Invalid Choice")      