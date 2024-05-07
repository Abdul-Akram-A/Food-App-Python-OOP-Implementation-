from Abstract import Abstract
class FoodItem(Abstract):
    def __init__(self,name,ratings,price,description):
        super().__init__(name,ratings)
        self.price = price
        self.description = description