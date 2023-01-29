from unittest import TestCase, mock
from le_main import le_data, something

class TestSomething(TestCase):

    def test_something(self):
        with mock.patch('le_main.le_data', return_value='thing'):
            self.assertEqual(something(), 'thing')
    
    def test_notherone(self):
        with mock.patch('le_main.le_data', return_value='thing'):
            self.assertEqual(le_data(), 'thing')