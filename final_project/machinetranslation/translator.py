# Author : Eric Kouassi
# Contact : hello@erickouassi.com
"""
This function return translation french to english
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

## Example for the Dallas location
# from ibm_watson import LanguageTranslatorV3
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# Authentication
authenticator = IAMAuthenticator("-YZ8yTFvzdBEhSNR1Yw6O2XYibUgjLKJTP8kRQpv5lf6")
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)

language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/99f4129b-9e31-42e7-bc71-8c48c24a25bf")

# e2f_translator_function
def english_to_french(english_text):
    """
    translate english to french
    """
    if english_text is None:
        return None
    french_text = language_translator.translate(
        text=english_text, model_id="en-fr"
    ).get_result()["translations"][0]["translation"]
    return french_text


# f2e_translator_function
def french_to_english(french_text):
    """
    translate french to english
    """
    if french_text is None:
        return None
    english_text = language_translator.translate(
        text=french_text, model_id="fr-en"
    ).get_result()["translations"][0]["translation"]
    return english_text
