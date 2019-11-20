import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test the employee class"""

    def setUp(self):
        """ Create an Employee class to use for all test methods"""
        self.emp = Employee('Althafuddin', 'Shaik', 112000)
        
    def test_give_default_raise(self):
        """Test the employee salary raise with default 5000"""
        self.emp.give_raise()
        self.assertEqual(117000, self.emp.salary)
    
    def test_give_custom_raise(self):
        """Test the employee salary raise with 10000"""
        self.emp.give_raise(10000)
        self.assertEqual(122000, self.emp.salary)

if __name__ == "__main__":
    unittest.main()