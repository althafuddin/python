from city_functions import get_city_name

print("Please enter 'q' to exit the program at any time!!!")
while True:

    city_name = input('\nPlease enter a city name: ')
    if city_name == 'q':
        break
    country_name = input('Please enter a country name: ')
    if country_name == 'q':
        break

    print(f"\t Formatted City Name:{get_city_name(city_name, country_name)}")