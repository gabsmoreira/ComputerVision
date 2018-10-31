from flask import Flask, request, jsonify, Response
import json
import io
import base64
import numpy as np
import cv2 as cv
import time
from gluoncv import model_zoo, data, utils
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import pickle

CLASSES = ('aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable',
 'dog', 'horse', 'motorbike', 'person', 'pottedplant',
 'sheep', 'sofa', 'train', 'tvmonitor')

app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/image', methods = ['POST'])
def getimage():
	if  request.method == 'POST':
		label = json.loads(request.data)['img']
	

	pickle_in = open("./files/processed_labels_inverse.pickle","rb")
	list_images_labels = pickle.load(pickle_in)
	results_paths = list_images_labels[label]
	# print(list_images_labels)

	pickle_in = open("./files/processed.pickle","rb")
	list_images_processed = pickle.load(pickle_in)    
	count = 0
	for path in results_paths:
		for image_processed in list_images_processed:
			if(path == image_processed[0]):
				class_IDs = image_processed[1]
				scores = image_processed[2]
				bounding_boxs = image_processed[3]
		img = cv.imread(path)
		img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
		# ax = utils.viz.plot_bbox(img, bounding_boxs[0], scores[0],
		# 										 class_IDs[0], class_names=CLASSES)
		# ax.get_figure().savefig(str(count) + '.jpg')
		count +=1
		# break
	# results_paths = [r[0] for r in results_paths]
	# for l in list_images_labels:
	# 	if label in l:
	# 		print(l[0])
	# 		results_paths.append(l[0])

	results = []
	count = 0
	for path in results_paths:
			# img = cv.imread(str(count) + '.jpg')
			img = cv.imread(path)
			# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
		# encode image as jpeg
			_, img_encoded = cv.imencode('.jpg', img)
			results.append(str(base64.b64encode(img_encoded)))
			count +=1
	if(len(results) == 0):
		img = cv.imread('./img/noimagefound.jpg')
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