from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model S', 2019)

print(f"--------\nCar: {my_tesla.get_descriptive_name()}")
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.get_software_update()

print(f"Updating the odometer")
my_tesla.update_odometer(3000)
print(f"Checking the software update status....")
my_tesla.get_software_update()


for i in range(8):
    print(f"\n----Going on a trip: \nStart Reading:{my_tesla.read_odometer()}")
    my_tesla.increment_odometer(1000)
    print(f"----Trip Completed: \nFinish Reading:{my_tesla.read_odometer()}")

print(f"Checking the software update status....")
my_tesla.get_software_update()

print(f"Upgrading the Battery...")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()