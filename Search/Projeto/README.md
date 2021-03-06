# Image Search Engine

The image search engine is used to search for look alike images given an initial image.


## Results
  ### Input
  <img src='./results/ele0.png'>

  ### Output
  <img src='./results/ele1.png'>


  <img src='./results/ele2.png'>

  -----

  ### Input
  <img src='./results/garfield0.png'>

  ### Output
  <img src='./results/garfield1.png'>


  <img src='./results/garfield2.png'>


  <img src='./results/garfield3.png'>



## Preparing your enviroment

Download the dataset CALTECH 101_ObjectCategories.


### Create vocabulary file

Run ```create_vocab.py``` to create the vocabulary for each image.


## Running without interface 
Run ```python main.py <image_path> ```.

The program will return the path and distance of the 5 most look alike images.

## Running with interface 

### Run backend
Run ```server.py ```.

### Run frontend
Turn CORS (Allow-Control-Allow-Origin) on. 

Go to ```/interface ``` and run ```yarn install ``` to install dependencies.

Then run ```yarn  start```. A webpage should pop in.

## How to deploy
Go to ```/interface ``` and run ```yarn install ``` to install dependencies. 

Run ```yarn build```. This should create another directory ```/build``` with static files for your website.

Run ```yarn add serve```.

Run ```yarn serve -s build ```. The static website should be running on your port 5000.
