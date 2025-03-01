class Vehicle:
  def __init__(self, brand, model, year, rental_price_per_day):
    self.brand = brand
    self.model = model
    self.year = year
    self.__rental_price_per_day = rental_price_per_day

  def get_rental_price_per_day(self):
    return self.__rental_price_per_day
  

  def set_rental_price_per_day(self, price):
    if price > 0:
      self.__rental_price_per_day = price
    else:
      print("Price should be greater than ZERO")



  def display_info(self):
    print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Rental Price per Day: ${self.get_rental_price_per_day()}")
  


class Car(Vehicle):
  def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
    super().__init__(brand, model, year, rental_price_per_day)
    self.seating_capacity = seating_capacity


class Bike(Vehicle):
  def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
    super().__init__(brand, model, year, rental_price_per_day)
    self.engine_capacity = engine_capacity