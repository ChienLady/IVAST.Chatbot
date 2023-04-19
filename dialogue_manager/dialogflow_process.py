from google.cloud import dialogflow_v2beta1 as dialogflow
from uuid import uuid4

from dialogue_manager import SESSION_CLIENT, CLOUD_PROJECT
from dialogue_manager.cache_manager import cache_check, cache_append, cache_get, cache_delete

def create_session(session_id: str) -> str:
    session = SESSION_CLIENT.session_path(CLOUD_PROJECT, session_id)
    return session

def answer(text: str, session_id: str = ''):
    if not cache_check(session_id):
        session_id = str(uuid4())
        session = create_session(session_id)
        cache_append(session_id, session = session)
    else:
        session = cache_get(session_id, ['session'])
    
    text_input = dialogflow.TextInput(text = text, language_code = 'vi-VN')
    query_input = dialogflow.QueryInput(text = text_input)

    response = SESSION_CLIENT.detect_intent(
        request={'session': session, 'query_input': query_input}
    )

    parameters = response.query_result.parameters
    answer = response.query_result.fulfillment_text
    intent = response.query_result.intent.display_name
    confidence = response.query_result.intent_detection_confidence
    print(parameters, answer, intent, confidence)

if __name__ == '__main__':
    answer('khỏe không')




