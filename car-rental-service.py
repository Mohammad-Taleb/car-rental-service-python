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
    print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Rental Price per Day: ${self.get_rental_price_per_day()}, ")
  


class Car(Vehicle):
  def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
    super().__init__(brand, model, year, rental_price_per_day)
    self.seating_capacity = seating_capacity
  
  def display_info(self):
   super().display_info()
   print(f"Seating Capacity: {self.seating_capacity}")


class Bike(Vehicle):
  def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
    super().__init__(brand, model, year, rental_price_per_day)
    self.engine_capacity = engine_capacity

  def display_info(self):
    super().display_info()
    print(f"Engine Capacity: {self.engine_capacity}cc")

















car = Car("Toyata", "Camry", 2022, 50 , 5)
bike = Bike("Yamaha", "YZF-R3", 2021, 30, 321)




while True:
  print("*************************************************")
  print()
  print("1 ==> To choose a Vehicle")
  print("2 ==> To enter how many days to rent out")
  print("3 ==> To show the updated prices")
  print("4 ==> To show your chosen vehicle info")
  print("0 ==> To exit the program")
  print()
  print("*************************************************")

  
  choice = int(input("Choose a number from the menu: "))

  if choice == 1:
    vehicleChoice = input("Car or Bike ?: ").lower()
    #UserVehicleChoice()