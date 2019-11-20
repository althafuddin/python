import unittest
from city_functions import get_city_name

class TestCityNames(unittest.TestCase):
    """Test the format given city name and country name"""

    def test_city_country(self):
        """Test the fucntion to work with 'hyderabad india'?"""
        formatted_name = get_city_name('hyderabad', 'india')
        self.assertEqual(formatted_name, 'Hyderabad, India')
    
    def test_city_country_population(self):
        """Test the function to work with 'seattle usa 100000' ?"""
        formatted_name = get_city_name('seattle', 'usa', population='100000')
        self.assertEqual(formatted_name, 'Seattle, Usa - Population 100000')
        

if __name__ == '__main__':
    unittest.main()