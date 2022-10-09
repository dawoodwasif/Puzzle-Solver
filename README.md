# Puzzle-Solver
## Objective
This program takes which can take this scrambled image, and return a string representing the ordering of the pieces that is required to unscramble this image.

## Methodology
First, divide each image into 4 equal rectangular pieces. Then pass each piece through the CNN. CNN extracts useful features and outputs a feature vector. We concatenate all 4 feature vectors into one using the Flatten layer. Then we pass this combined vector through a feed-forward network. The last layer of this network gives us a 16-unit long vector. We reshape this 16-unit vector into a matrix of 4x4.

## Instruction
Model weights are provided in model.h5. Use the code in submission.py of make prediction function in Prediction class to run model on image path. Them ain.ipynb notebook has the main training code which is reproducible.

Model Weights: https://drive.google.com/drive/folders/1-qw3nWjxU_f9X2sczc49I-tUTsesJs5o?usp=sharing
Dataset: https://drive.google.com/file/d/1tQTwXA3Z_ISTAZPScEz8baUYqgafRtpQ/view
