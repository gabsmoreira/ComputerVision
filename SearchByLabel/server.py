from flask import Flask, request, jsonify, Response
import json
import io
import base64
import numpy as np
import cv2 as cv
import time
import pickle

app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/image', methods = ['POST'])
def getimage():
	if  request.method == 'POST':
		label = json.loads(request.data)['img']
	

	pickle_in = open("processed_labels_inverse.pickle","rb")
	list_images_labels = pickle.load(pickle_in)
	results_paths = list_images_labels[label]
	for l in list_images_labels:
		if label in l:
			print(l[0])
			results_paths.append(l[0])

		results = []
		for path in results_paths:
				img = cv.imread(path)
			# encode image as jpeg
				_, img_encoded = cv.imencode('.jpg', img)
				results.append(str(base64.b64encode(img_encoded)))
		if(len(results) == 0):
			img = cv.imread('./noimagefound.jpg')
			# encode image as jpeg
			_, img_encoded = cv.imencode('.jpg', img)
			results.append(str(base64.b64encode(img_encoded)))
		# print(results)
	
	print("returning")
	return jsonify(results)



app.run(host='0.0.0.0', port=8001)



#('aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
#  'bus', 'car', 'cat', 'chair', 'cow', 'diningtable',
#  'dog', 'horse', 'motorbike', 'person', 'pottedplant',
#  'sheep', 'sofa', 'train', 'tvmonitor')