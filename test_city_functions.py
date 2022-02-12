import unittest
from city_functions import get_formatted_name


class NameTestCase(unittest.TestCase):
    """ Test for city_functions.py """

    def test_get_formatted_name(self):
        """ Testing for names like yangon, myanmar """
        formatted_name = get_formatted_name('yangon', 'myanmar')
        self.assertEqual(formatted_name, "Yangon,Myanmar")

    def test_get_formatted_name_population(self):
        """ Testing for names like yangon, myanmar - population 500000 """
        formatted_name = get_formatted_name('yangon', 'myanmar', 50000)
        self.assertEqual(formatted_name, "Yangon,Myanmar - 50000")


unittest.main()
