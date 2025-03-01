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
  

  def calculate_rental_cost(self,days):
    return self.get_rental_price_per_day() * days


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







def UserVehicleChoice():
  if vehicleChoice == 'car':
    car.display_info()
  elif vehicleChoice == 'bike':
    bike.display_info()
  else:
      print('Vehicle not available') 


def NumberOfDays():
  if days > 0:
    if vehicleChoice == 'car':
      car_rental_cost= car.calculate_rental_cost(days)
      print(f"Car rental cost for {days} days: ${car_rental_cost}")
    elif vehicleChoice == 'bike':
      bike_rental_cost= bike.calculate_rental_cost(days)
      print(f"bike rental cost for {days} days: ${bike_rental_cost}")
    else:
      print("You need to choose a VEHICLE first")
  else:
      print("Enter a vaild number of DAYS")


def NewPrices():
  if days > 0:
    if vehicleChoice == 'car':
      car.set_rental_price_per_day(55)  
      print(f"The new rental price per day for {car.brand}{car.model}: ${car.get_rental_price_per_day()}")
    elif vehicleChoice == 'bike':
      bike.set_rental_price_per_day(35)
      print(f"The new rental price per day for {bike.brand}{bike.model}: ${bike.get_rental_price_per_day()}")
    else:
      print("You need to choose a VEHICLE first")
  else:
      print("You need to choose how many DAYS first")


def ChosenVehicleInfo():
   if vehicleChoice == 'car':
      show_vehicle_info(car)
   elif vehicleChoice == 'bike':
      show_vehicle_info(bike)
   else:
      print("You need to choose a VEHICLE first")


def show_vehicle_info(vehicle):
  vehicle.display_info()




car = Car("Toyata", "Camry", 2022, 50 , 5)
bike = Bike("Yamaha", "YZF-R3", 2021, 30, 321)

vehicleChoice = None
days = 0



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
    UserVehicleChoice()
  
  elif choice == 2:
    days = int(input("Enter how many days you want to rent: "))
    NumberOfDays()

  elif choice == 3:
    NewPrices()

  elif choice == 4:
    ChosenVehicleInfo()

  elif choice == 0:
    print("PROGRAM EXIT")
    break