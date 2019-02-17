from flask import Flask, render_template, request, redirect
from twilio.rest import Client
from passwords import *
import jinja2
import os
from watson_developer_cloud.websocket import RecognizeCallback, AudioSource
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud.websocket import SynthesizeCallback
from os.path import join, dirname
import json
import requests

from watson_developer_cloud import SpeechToTextV1

app = Flask(__name__)
TEST_MODE = True
number = ''

@app.route('/')
def hello():
	print('hi')
	return 'oh'

@app.route('/change')
def chance():
	return redirect('/')

def send_sms():
	# TODO: Makena's code
	account_sid = TWILIO_ACCOUNT_SID
	auth_token = TWILIO_TOKEN
	client = Client(account_sid, auth_token)

	if not TEST_MODE:
		message = client.messages \
                .create(
                     body= "You are designated as " + USER_NAME + "'s emergency contact. \
                     They were stopped at " + STOP_TIME + " in " + STOP_LOCATION + ".",
                     from_='+18059792058',
                     to='+12016610120'
                 )

	# print(message.sid)

def start_audio_recording():
	# TODO: Start the audio recording
	return False

def stop_audio_recording():
	# TODO: STOP the audio recording and save it
	return False

def text_to_speech(text):
	_API_KEY = ''
	KEY_FILE = "keys.txt"
	with open(KEY_FILE, "r") as key_file:
		content = key_file.read().splitlines()
		_API_KEY = content[0]

	service = TextToSpeechV1(
    	iam_apikey=_API_KEY,
    	url='https://gateway-wdc.watsonplatform.net/text-to-speech/api'
	)

	with open(join(dirname(__file__), './'+'output'+'.wav'), 'wb') as audio_file:
		response = service.synthesize(
			text, accept='audio/wav',
			voice="en-US_MichaelVoice").get_result()
		audio_file.write(response.content)

def speech_to_text(speech_file):
	sst_api_key = 'e_jevakkc6QsQcCmA41mMtKE2sJl1Ug0OEoKEi8oLIb1'
	sst_url = 'https://stream.watsonplatform.net/speech-to-text/api'
	
	speech_to_text = SpeechToTextV1(
		iam_apikey=sst_api_key,
		url=sst_url
	)

	class MyRecognizeCallback(RecognizeCallback):
		def __init__(self):
			RecognizeCallback.__init__(self)

		def on_data(self, data):
			print(json.dumps(data, indent=2))

		def on_error(self, error):
			print('Error received: {}'.format(error))

		def on_inactivity_timeout(self, error):
			print('Inactivity timeout: {}'.format(error))

	myRecognizeCallback = MyRecognizeCallback()

	with open(join(dirname(__file__), './.', speech_file), 'rb') as audio_file:
		audio_source = AudioSource(audio_file)
		speech_to_text.recognize_using_websocket(
        audio=audio_source,
        interim_results=True,
        content_type='audio/wav',
        recognize_callback=myRecognizeCallback,
        keywords=['ticket'],
        keywords_threshold=0.8)

#text_to_speech('hello my name is donald and i am a president')
#peech_to_text('output.wav')

def send_next_steps():
	# TODO: sends the next steps / advice / how to access resources - depending
	# on the conversation that just happened with police
	return False

@app.route('/post', methods=['GET','POST'])
def post():
	if request.method == 'POST':
		return render_template('post.html')
	return render_template('get.html')

if __name__ == '__main__':
	#port = int(os.environ.get('PORT', 8000))
	#app.run(host='0.0.0.0', port=port,debug=True)
	app.run(debug=True)