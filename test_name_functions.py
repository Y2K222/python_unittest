import unittest
from name_functions import get_formatted_name


class NameTestCase(unittest.TestCase):
    """ Tests for name functions.py """

    def test_first_last_name(self):
        """ Do names like John Doe work ? """
        formatted_name = get_formatted_name('john', 'doe')
        self.assertEqual(formatted_name, "John Doe")

    def test_first_last_middle_name(self):
        """ Do names like Zaw Htet Aung work ? """
        formatted_name = get_formatted_name("zaw", "aung", "htet")
        self.assertEqual(formatted_name, "Zaw Htet Aung")


unittest.main()
