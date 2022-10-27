

class Happy_hour:
    def __init__(self, restaurant_name,restaurant_location,hh_duration,hh_price,):
        """ 
        This method initiates the class Happy_hour
        
        """
        self.name= restaurant_name,
        self.location=restaurant_location,
        self.duration=hh_duration,
        self.price=hh_price

    def change_restaurant_name(self, new_restaurant_name):
        self.name = new_restaurant_name
        return new_restaurant_name
        

    def change_hh_duration(self, new_happy_hour_duration):
        self.duration = new_happy_hour_duration
        return new_happy_hour_duration


    def change_hh_price(self,new_price):
        self.price =new_price
        return new_price


    

    
