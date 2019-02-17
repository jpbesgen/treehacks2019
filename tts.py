#!/usr/bin/env python3

from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud.websocket import SynthesizeCallback
import json
from os.path import join, dirname
import requests

_API_KEY = ''
KEY_FILE = "keys.txt"

with open(KEY_FILE, "r") as key_file:
    content = key_file.read().splitlines()
    _API_KEY = content[0]

service = TextToSpeechV1(
    iam_apikey=_API_KEY,
    url='https://gateway-wdc.watsonplatform.net/text-to-speech/api'
)

def generate_wave_file(filename, text):
    with open(join(dirname(__file__), './'+filename),
          'wb') as audio_file:
        response = service.synthesize(
            text, accept='audio/wav',
            voice="en-US_MichaelVoice").get_result()
        audio_file.write(response.content)