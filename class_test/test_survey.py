import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """ Test for the AnonymousSurvey class"""

    def setUp(self):
        """ Create a example survey """
        test_question = "Test question ?"
        self.test_survey = AnonymousSurvey(test_question)

    def test_store_response(self):
        """ Test that single response  is stored correctly"""
        self.test_survey.store_response("zaw")
        self.assertIn("Zaw", self.test_survey.responses)

    def test_store_three_response(self):
        """ Test that the function can handle three responses """
        responses = ["One", "Two", "Three"]
        for response in responses:
            self.test_survey.store_response(response)

        for response in responses:
            self.assertIn(response, self.test_survey.responses)


unittest.main()
