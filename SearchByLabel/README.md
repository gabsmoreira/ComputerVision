# Image Label Search Engine 

This image label search engine was created using ```ssd_512_resnet50_v1_voc``` from GluonCV.

## Preparing your enviroment

Download the dataset from Dropbox.


### Create labels file

Run ```prepare.py``` and ```labelize.py``` to create path-to-label dictionary.

Run ```inverse_label.py``` to create label-to-path dictionary.


## Running without interface 
Run ```python search_test.py <label> ```.

The program will return the path of every image identified with this label.


## Running with interface 

### Run backend
Run ```server2.py ```.


### Run frontend
Turn CORS (Allow-Control-Allow-Origin) on. 

Go to ```/interface ``` and run ```yarn install ``` to install dependencies.

Then run ```yarn  start```. A webpage should pop in.

## How to deploy
Go to ```/interface ``` and run ```yarn install ``` to install dependencies. 

Run ```yarn build```. This should create another directory ```/build``` with static files for your website.

Run ```yarn add serve```.

Run ```yarn serve -s build ```. The static website should be running on your port 5000.
