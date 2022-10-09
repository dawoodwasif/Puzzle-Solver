# Puzzle-Solver
## Objective
This program takes which can take this scrambled image, and return a string representing the ordering of the pieces that is required to unscramble this image.

## Methodology
First, divide each image into 4 equal rectangular pieces. Then pass each piece through the CNN. CNN extracts useful features and outputs a feature vector. We concatenate all 4 feature vectors into one using the Flatten layer. Then we pass this combined vector through a feed-forward network. The last layer of this network gives us a 16-unit long vector. We reshape this 16-unit vector into a matrix of 4x4.
