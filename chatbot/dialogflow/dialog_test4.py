import yaml
from google.cloud import dialogflow

data = yaml.full_load(open('data.yaml'))
courses = []
attributes = []

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

def get_course_entities(result):
    parameters = result.query_result.parameters
    for parameter in parameters:
        if str(parameter) == 'course_entity':
            return parameters[parameter]
    return []

def get_attribute_entities(result):
    parameters = result.query_result.parameters
    for parameter in parameters:
        if str(parameter) == 'attribute_entity':
            return parameters[parameter]
    return []

def get_modified_reponse():
    # print(courses)
    response = ''
    for course in courses:
        if attributes != []:
            for attribute in attributes:
                course_data = data[course]
                attribute_data = course_data[attribute.lower()]
                response_from_dialogflow = df.get_response_text()
                r = response_from_dialogflow.replace('__ic__', course_data['ic']).replace('__units__', str(course_data['units'])).replace('__code__', course_data['code']).replace('__course__', course).replace('__attribute__', attribute).replace('__attribute_value__', str(attribute_data))
                if not r in response:
                    response += '\n' + r
        else:
            course_data = data[course]
            # attribute_data = course_data[attribute.lower()]
            response_from_dialogflow = df.get_response_text()
            r = response_from_dialogflow.replace('__ic__', course_data['ic']).replace('__units__', str(course_data['units'])).replace('__code__', course_data['code']).replace('__course__', course)
            if not r in response:
                response += '\n' + r
    return response



if __name__ == "__main__":
    df = Dialogflow('bot-test-303915')
    while True:
        print('\n\n\n\n\n\n')
        question = input('Question: ')
        result = df.get_response(question)
        courses = get_course_entities(result) or courses
        attributes = get_attribute_entities(result) or attributes
        if courses == []:
                print(df.get_response_text())
        else:
                print(get_modified_reponse())

        
