import json
import pickle
import numpy as np
from flask import Flask
from flask import request


app = Flask(__name__)

with open("clf.pkl", "rb") as f:
    clf = pickle.load(f)


def __process_input(request_data: str) -> np.array:
    return np.array(np.asarray(json.loads(request.data)["data"]))


# Creating route for model prediction
@app.route("/predict", methods=["POST"])
def predict() -> str:
    input_params = __process_input(request.data)
    print(len(input_params))
    if request.method == "POST":
        try:
            prediction = clf.predict(input_params)
            return json.dumps({"predicted_price ($1000s)": list(prediction.tolist())})
        except:
            return json.dumps({"error": "PREDICTION FAILED"}), 400