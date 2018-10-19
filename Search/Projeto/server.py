from flask import Flask, request, jsonify, Response
import json
import io
import base64
import numpy as np
import cv2 as cv
import time
from lib import *

app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/image', methods = ['POST'])
def getimage():
	if  request.method == 'POST':
		img = json.loads(request.data)['img'].encode("utf-8")
		# print(img[22:])
		fh = open("imageToSave.jpeg", "wb")
		fh.write(base64.decodebytes(img[22:]))
		fh.close()

		DATASET = ["Faces", "garfield", "platypus", "nautilus", "elephant", "gerenuk"]


		pickle_in = open("paths.pickle","rb")
		paths = pickle.load(pickle_in)

		pickle_in = open("vocab.pickle","rb")
		vocab = pickle.load(pickle_in)

		pickle_in = open("hist.pickle","rb")
		hist_list = pickle.load(pickle_in)

		s_list = search("imageToSave.jpeg", vocab, hist_list, paths)
		results = []
		for i in range(5):
			print(f"""
	Distance: {s_list[i][0]}
	Imagem: {s_list[i][1]}                  
	-------------------------------- """)
		for i in range(5):
				img = cv.imread(s_list[i][1])
			# encode image as jpeg
				_, img_encoded = cv.imencode('.jpg', img)
				results.append(str(base64.b64encode(img_encoded)))
		# print(results)
	
	print("returning")
	return jsonify(results)



app.run(host='0.0.0.0', port=8001)