my-ml-jacket
============

A collection of explorations around ML methodologies and tools, using

[sklearn](http://scikit-learn.org/stable/)

[tflearn](https://github.com/tflearn/tflearn)

### Problem

As a user, I want to receive recommendations on the next table header to
add, given the history of other users' headers on the site.

Idea being - if I'm typing in "Appetizers", then "Main Dish", then the
recommender might suggest my next entry be "Dessert", based on prior
data.

Similarly, "Breakfast" may be followed by "Lunch", then "Dinner".

### Dataset

Dataset is extracted from anonymized Wejoinin table header (row/column)
data.

## Installing Tensorflow

Instructions here: https://www.tensorflow.org/install/install_mac

Remember to source the virtualenv environment. In this example, we have
set virtualenv to set up a virtual environment in
`~/workspace/tensorflow`:

    $ source ~/workspace/tensorflow/bin/activate

Do this before attempting to start TF.
