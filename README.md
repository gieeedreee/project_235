# Predicting the price of house

This project is about training a simple regression model ('Gradient boosted tree') that can predict house price. The model is in 'prediction.py' file.

Other part of this project is to creat API for the trained model. The Flask app you can find in 'app.py' file.
This file contains the code, for running the Web API of the final model (which was saved as "clf.pkl" and then loaded in 'app.py') chosen after model evaluation.


Here are all packages required for running the Web API:
* numpy

* flask

* sklearn

* gunicorn

* pickle

* json
