from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

with open("../ml/model.pkl", "rb") as f:
    model, encoder = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[
        data["temperature"],
        data["humidity"],
        data["moisture"],
        data["ph"]
    ]])

    prediction = model.predict(features)
    crop = encoder.inverse_transform(prediction)[0]

    return jsonify({
        "recommended_crop": crop
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
