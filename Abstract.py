from abc import ABC
class Abstract(ABC):
    def __init__(self,name,rating=None):
        self.name = name
        self.rating=rating
        
    