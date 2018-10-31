"""1. Predict with pre-trained SSD models
==========================================

This article shows how to play with pre-trained SSD models with only a few
lines of code.

First let's import some necessary libraries:
"""

from gluoncv import model_zoo, data, utils
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import os
import pickle
import numpy

labels = []
net = model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained=True)
# PATH = './dataset-projeto-3-2/gabrielfm2/sheep5.jpg'

pickle_in = open("processed.pickle","rb")
list_images_processed = pickle.load(pickle_in)    

for image_processed in list_images_processed:
  image_label = []
  image_label.append(image_processed[0])
  class_IDs = image_processed[1]
  scores = image_processed[2]
  bounding_boxs = image_processed[3]

  scores = scores.asnumpy()
  class_IDs = class_IDs.asnumpy()
  bounding_boxs = bounding_boxs.asnumpy()
# print(net.classes)

  for i in range(len(class_IDs[0])):
    if(scores[0][i] > 0.6):
      index = int(class_IDs[0][0][0])
      if(net.classes[index] not in image_label):
        image_label.append(net.classes[index])
      # print(net.classes[index])
  labels.append(image_label)

pickle_out = open("processed_labels.pickle","wb")
pickle.dump(labels, pickle_out)
# print(class_IDs[0][0][0])
# print(net.classes[0])
# print(class_IDs[0])
# for score in scores[0]:
#   if(score[0] > 0.5):
#     print(score[0])
# print()
# print(net.classes[class_IDs[0][0]])

# x, img = data.transforms.presets.ssd.load_test(PATH, short=512)
# ax = utils.viz.plot_bbox(img, bounding_boxs[0], scores[0],
#                          class_IDs[0], class_names=net.classes)

# plt.show()
