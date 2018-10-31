# Image Label Search Engine 

## How to run

### Preparing your enviroment
Download the dataset from Dropbox.


### Create labels file

Run ```prepare.py``` and ```labelize.py``` to create path-to-label dictionary.

Run ```inverse_label.py``` to create label-to-path dictionary.

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
