
from google.cloud import dialogflow
class Dialogflow:

    def __init__(self, project_id, session_id=123456789):
        self.__project_id = project_id
        self.__session_id = session_id
        self.__session_client = dialogflow.SessionsClient()
        self.__session = self.__session_client.session_path(project_id, session_id)

    def get_response(self, text, language_code='en'):
        '''Returns response object using session_client object'''
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        self.__response = self.__session_client.detect_intent(
            request={"session": self.__session, "query_input": query_input}
        )
        # print(self.__response)
        return self.__response

    def get_response_text(self, response=None):
        if not response:
            response = self.__response
        # return response.query_result.fulfillment_text
        return response.query_result.fulfillment_text

    def get_response_confidence(self, response=None):
        if not response:
            response = self.__response
        return response.query_result.intent_detection_confidence

    # def create_intent(name):
    #     parent = f'projects/{self.__project_id}/agent'
    #     intent = dialogflow.Intent(display_name=name, )

if __name__ == "__main__":
    df = Dialogflow('bot-test-303915')
    while True:
        question = input('Question: ')
        df.get_response(question)
        print(df.get_response_text())
        # print(df.get_response_confidence())