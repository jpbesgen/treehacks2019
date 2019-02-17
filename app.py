from flask import Flask, render_template, request, redirect
from flask_cors import CORS
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

from watson_developer_cloud import VisualRecognitionV3
import time, operator
import cv2
import vlc

from watson_developer_cloud import SpeechToTextV1
from playsound import playsound



app = Flask(__name__)
CORS(app) 

TEST_MODE = False
number = ''

@app.route('/', methods=['GET'])
def hello():
	print('hi')
	return 'oh'

@app.route('/change')
def chance():
	return redirect('/')

@app.route('/sound_calm', methods=['POST'])
def sound_calm():
	p = vlc.MediaPlayer('./sounds/mom.mp3')
	p.play()
	# playsound('./sounds/mom.mp3')
	#playsound('./sounds/siren.wav')
	return ""

# @app.route('/stop', methods=['POST'])
# def stop_playing(p):
# 	p.stop()

@app.route('/sound_encounter', methods=['POST'])
def sound_encounter():
	playsound('encounter.wav')
	return ""

@app.route('/send_sms', methods=['POST'])
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
	return True
	# print(message.sid)

def classify_image(img):
	visual_recognition = VisualRecognitionV3(version='2018-03-19', iam_apikey='s5JSfY9-Eb14tzcA6xBkWoYmVpIF9eJFIHlutgUYBMcP')

	with open(img, 'rb') as images_file:
		#print(img)
		classes = visual_recognition.classify(
			images_file,
			threshold='0.5',
			owners=["IBM"]).get_result()
		# j = json.dumps(classes, indent=2)
		items = classes['images'][0]['classifiers'][0]['classes']
		labels_scores_dict = {}

		for i in items:
			labels_scores_dict[i['class']] = i['score']

		#print(labels_scores_dict)
		print()

		results = []
		for k, v in labels_scores_dict.items():
			if k == 'police cruiser':
				results.append(k)
				return json.dumps(results)

		for key, value in sorted(labels_scores_dict.items(), key=operator.itemgetter(1), reverse=True)[-3:]:
			if key != 'police cruiser':
				results.append(key)

		return json.dumps(results)

@app.route('/record', methods=['GET'])
def begin_classification():

	camera = cv2.VideoCapture(0)

	# for i in range(1):
		#if i % 50 == 1:
			#print(i)
	return_value, image = camera.read()
	cv2.imwrite('test_images/opencv.png', image)
	results = classify_image('test_images/opencv.png')
	del(camera)
	return str(results)
		

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
        keywords=['ticket', 'speeding', 'limit', 'cell phone', 'cellphone', 'seatbelt', 'tailgating'],
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