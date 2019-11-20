from car import Car

my_new_car = Car('hyundai', 'sonata', 2019)
print(my_new_car.get_descriptivve_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()