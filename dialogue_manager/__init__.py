import os
import json
from google.oauth2 import service_account
from google.cloud import dialogflow_v2beta1 as dialogflow

with open(os.path.join('dialogue_manager', 'configs', 'dialogflow_credential.json'), 'r') as f:
    dialogflow_key = json.load(f)
credentials = (service_account.Credentials.from_service_account_info(dialogflow_key))
SESSION_CLIENT = dialogflow.SessionsClient(credentials=credentials)

CLOUD_PROJECT = os.getenv('CLOUD_PROJECT', 'ivast-chatbot-jbj9')
