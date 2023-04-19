from google.cloud import dialogflow_v2beta1 as dialogflow
from google.oauth2 import service_account
import os
import json

with open('F:\IVAST.Chatbot\dialogue_manager\configs\dialogflow_credential.json', 'r') as f:
    dialogflow_key = json.load(f)
    
credentials = (service_account.Credentials.from_service_account_info(dialogflow_key))

session_client = dialogflow.SessionsClient(credentials=credentials)
session = session_client.session_path('ivast-chatbot-jbj9', 'abcd')

print("Session path: {}\n".format(session))

text = 'khỏe không'
text_input = dialogflow.TextInput(text=text, language_code='vi-VN')

query_input = dialogflow.QueryInput(text=text_input)

response = session_client.detect_intent(
    request={"session": session, "query_input": query_input}
)

print("=" * 20)
print("Query text: {}".format(response.query_result.query_text))
print(
    "Detected intent: {} (confidence: {})\n".format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence,
    )
)
print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))

