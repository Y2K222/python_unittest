class AnonymousSurvey:
    """ Collect anonymous answers to survey questions """

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_questions(self):
        """ Show all quuestions """
        print(self.question)

    def store_response(self, new_response):
        """ Function to store single response """
        self.responses.append(new_response.title())

    def show_results(self):
        """ Show all reponses that have been given"""
        print("Survey results : ")
        for response in self.responses:
            print("\n - " + response)
