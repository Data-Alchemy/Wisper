import os
import openai
import pandas as pd
import json
import speech_recognition as sr
import pyttsx3


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth',None)

class Analyzer():

    '''
    This class enables communication with wisper api
    '''

    def __init__(self,org, key):
        self.org = org
        self.key = key

    def voice_to_text():
    # initialize the recognizer
        r = sr.Recognizer()

        # use the microphone as source for input
        with sr.Microphone() as source:
            print("Speak now...")
            # adjust for ambient noise
            r.adjust_for_ambient_noise(source)
            # listen for the user's voice input
            audio = r.listen(source)

        try:
            # recognize the speech using Google Speech Recognition
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


    def text_to_voice(text):
        # initialize the engine
        engine = pyttsx3.init()
        # set the voice properties
        voices = engine.getProperty('voices')
        # change voice index for desired voice
        engine.setProperty('voice', voices[0].id)
        # say the text
        engine.say(text)
        # wait for the speech to finish
        engine.runAndWait()


    def model_list(self):
        openai.organization = self.org
        openai.api_key = self.key
        models = openai.Model.list()
        return json.dumps(models)
    
    def completion(self):
        openai.api_type = "azure"
        openai.api_key = self.key
        openai.api_base = "https://example-endpoint.openai.azure.com"
        openai.api_version = "2022-12-01"
        completion = openai.Completion.create(engine="deployment-name", prompt="Hello world")
        return print(completion.choices[0].text)

