from flask import Flask, render_template, request, redirect
from twilio.rest import Client
from passwords import *
import jinja2
import os

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

	if TEST_MODE:
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
	app.run()