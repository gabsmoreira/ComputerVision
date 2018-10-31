import pickle

pickle_in = open("./files/processed_labels.pickle","rb")
list_images_labels = pickle.load(pickle_in)
results_paths = []

d = {}

for i in range(len(list_images_labels)):
  path = list_images_labels[i][0]
  for j in range(1,len(list_images_labels[i])):
    label = list_images_labels[i][j]
    print(label)
    if(label in d):
      print(path)
      d[label].append(path)
    else:
      d[label] = []


pickle_out = open("./files/processed_labels_inverse.pickle","wb")
pickle.dump(d, pickle_out)

print(d)