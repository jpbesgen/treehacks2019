import json
from watson_developer_cloud import VisualRecognitionV3
import time, operator
import cv2

camera = cv2.VideoCapture(0)
visual_recognition = VisualRecognitionV3(version='2018-03-19', iam_apikey='s5JSfY9-Eb14tzcA6xBkWoYmVpIF9eJFIHlutgUYBMcP')

def classify_image(img):
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
				return results

		for key, value in sorted(labels_scores_dict.items(), key=operator.itemgetter(1), reverse=True)[-3:]:
			if key != 'police cruiser':
				results.append(key)

		return results

for i in range(1000):
	if i % 50 == 1:
		#print(i)
		return_value, image = camera.read()
		cv2.imwrite('test_images/opencv'+str(i)+'.png', image)
		classify_image('test_images/opencv'+str(i)+'.png')
		
del(camera)

#url = 'https://c8.alamy.com/comp/CN189B/view-in-rear-view-mirror-traffic-police-car-drink-driving-christmas-CN189B.jpg'
