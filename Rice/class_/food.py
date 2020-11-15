

class Food:
    def __init__(self, rice = None, meat = None ,cost = None):
        self.rice = rice
        self.meat = meat
        self.cost = cost
    
    def  food_info(self):
        return(self.rice, self.meat, self.cost)
    
    def __repr__(self):
        return f"(Rice type: {self.rice}, Meat: {self.meat}, Cost: {self.cost})"