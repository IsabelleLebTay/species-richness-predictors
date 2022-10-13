# species-richness-predictors

# Is relative closeness to a human induced disturbnca a strong predictor of bird community richness and composition?

The response variables are species richness and composition. The predictors included in the analysis are vegetation info and closeness to each disturbance type.

# Model: Random Forest 
A Random Forest algorithm is a machine learning model that makes individual decision trees, averages their output, and uses a importance indicator of the predictors. Each decision tree can be sensitive to trends, but the entire process is relatively robust against overfitting.

## Some terminology
Classes: the values of the predictor. In this dataset, the classes are each unique value we calculated for species richness.

Features: there are 

The classifier trains on a subset of the data

The predictors and response variables can be categorical, discrete, or continuous.
RF tends to perform worse when the classes are inbalanced. This occurs in datasets where there are a lot of zeros, such as samples fololwing a Poisson distribution. Species occupancy models are one such example, where the imbalance of the classes (more weight towards zero detections) should be taken into account when conducting the models. Since it is possible we have unbalanced classes, we will quickly check how many sites belong tp each species richness class.


