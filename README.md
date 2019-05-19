# Dog Breed Classifier

The aim of this repository is to gain some familiarity with TensorFlow and use deep learning to build a model which performs well at identifying the breed of a dog, given an image of a dog.

Kaggle Competition- https://www.kaggle.com/c/dog-breed-identification

Data available- https://www.kaggle.com/c/dog-breed-identification/data

## Data 
* Data contains 120 breeds of dogs
* From a brief manual sample of some of the images in the training dataset, it would appear that some of the images have more than one dog (including different breeds) and quite a few have people in as well. 
* The training data consists of 10,222 images (JPG files) of dogs.
* There is a seperate label CSV file that provides that contains the id of the image and the breed of the dog present in the photo
* Test set contains 10,357 images (JPG files) of dogs
* The height and width of images in the training and test sets varies a lot (some sort of preprocessing will be required)

## Evaluation
* metric used for evaluation is multi class log loss
* the submission file should contain the id of the test image as well as the predicted probability for each of the 120 breeds for a given image

## Training
Have trained a basic CNN for 3 epochs. Have tried to train the model for more epochs locally, but I'm not able to on my current machine. Plan is to use SageMaker
to build a advanced model. 

At the AWS Summit 2019 there was a demo of "script mode" on a SageMaker Notebook instance. It showed the ability of being able
to train a custom Keras model, defined in a Python script, using a SageMaker training instance. The plan is it use this
to be able to train the model for more epochs. 

Script mode examples:

* [AWS example](https://github.com/aws-samples/amazon-sagemaker-script-mode)

* [example from summit breakout session](https://gitlab.com/juliensimon/dlnotebooks)