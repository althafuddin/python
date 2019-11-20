def get_city_name(city, country, population=''):
    """Format the city name and country names"""
    if population:
        formatted_name = f"{city}, {country} - population {population}"
    else: 
        formatted_name = f"{city}, {country}"
    return formatted_name.title()