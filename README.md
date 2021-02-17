# Predicting the price of house

This project is about training a simple regression model ('Gradient boosted tree') that can predict house price. The model is in 'prediction.py' file.

Second part of this project is to creat API for the trained model. The Flask app you can find in 'app.py' file.
This file contains the code, for running the Web API of the final model (which was saved as "clf.pkl" and then loaded in 'app.py') chosen after model evaluation.


The third part of this project is Deploying Flask App on Heroku.
Here are some steps how to do it:
1. Initialize an empty repo, add the files in the repo and commit all the changes:
    $ git init 
    $ git add .
    $ git commit -m "Initial Commit"
2. Login to heroku CLI using: heroku login
3. Create a unique name for your Web app.
    $ heroku create <app name>-app
4. Push your code from local to the heroku remote.
    $ git push heroku master
5. Finally, web app will be deployed on http://<app name>.herokuapp.com (instead of <app name> use your app name).

The best tool for making HTTP requests is Postman. Here is the link which should be used for creating a request:
https://<app name>.herokuapp.com/predict
There is only POST request in this project and requests should be made in this format (POST/ write link/ choose body/ raw/ copy request and SEND):
{"data": [[20, 0, 4.1, 0, 0.368, 4.906, 90, 1.1742, 4, 666,20.2, 396.9, 34.77]]}

Here are all packages required for running the Web API:
numpy

flask

sklearn

gunicorn

pickle

json
