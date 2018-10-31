import pickle
import sys
import pprint
pickle_in = open("./files/processed_labels_inverse.pickle","rb")
list_images_labels = pickle.load(pickle_in)
search_label = sys.argv[1]
results_paths = list_images_labels[search_label]
print(f"Images with {search_label}")
pprint.pprint(results_paths)