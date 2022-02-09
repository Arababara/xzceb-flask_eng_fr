"""class docstring"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('intHhIt_3_-Ep2NfOkinejqp_HGoDS0e5Y_IRyVnXg1y')
language_translator = LanguageTranslatorV3(
    version ='2018-05-01',
    authenticator = authenticator
)
language_translator.set_service_url(
    'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/b1040d0d-7f57-461e-9095-c2428291be0c'
    )

def english_to_french(english_text):
    #write the code here
    """class docstring
    code to translate english text to french"""
    translation = language_translator.translate(
        text = english_text, model_id = "en-fr"
        ).get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    #write the code here
    """code to translate french text to english
    class docstring"""
    translation = language_translator.translate(
        text = french_text, model_id = "fr-en"
        ).get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
