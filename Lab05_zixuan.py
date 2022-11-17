
class Vehicle:
    engine_capacity = "1,6 Turbo"

    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def drive(self):
        print("The vehicle is in driving mode now.")

vios = Vehicle ('4', 'petrol', 5, 180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)
vios.drive()

class ElectricCar(Vehicle):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Vehicle.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)

blueSG = ElectricCar ('4', 5, 150)
blueSG.drive()

class Computer:
    def __init__(self, CPU_speed, type_of_computer, memory_size, harddisk_size):
        self.CPU_speed = CPU_speed
        self.type_of_computer = type_of_computer
        self.memory_size = memory_size
        self.harddisk_size = harddisk_size

    def playGame(self):
        print('My '+ self.type_of_computer + ' is playing the game now!')

class Desktop(Computer):
        def __init__(self, CPU_speed, type_of_computer , memory_size, harddisk_size):
          Computer.__init__(self, CPU_speed, 'Desktop', memory_size, harddisk_size)


class Laptop(Computer):
    def __init__(self, CPU_speed, type_of_computer, memory_size, harddisk_size):
        Computer.__init__(self, CPU_speed, 'Laptop', memory_size, harddisk_size)

macbook = Laptop('1.7GHz','','16GB','2TB')
print(macbook.CPU_Speed)
print(macbook.type_of_computer)
print(macbook.memory_size)
print(macbook.harddisk_size)
macbook.PlayGame()