import pickle

search_label = 'aeroplane'

pickle_in = open("processed_labels.pickle","rb")
list_images_labels = pickle.load(pickle_in)

for label in list_images_labels:
  if search_label in label:
    print(label[0])


