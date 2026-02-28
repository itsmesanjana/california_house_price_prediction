from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
obj = joblib.load('california_house_price_prediction_model.joblib')
model = obj['model']
columns = obj['columns']


@app.route("/")
def home():
    return render_template("index.html", columns=columns)


# 🔥 HTML form prediction
@app.route("/predict", methods=["POST"])
def predict():

    inputs = []
    for col in columns:
        value = request.form.get(col, type=float)
        inputs.append(value)

    prediction = model.predict([inputs])[0]

    return render_template(
        "result.html",
        prediction=round(prediction, 3)
    )


# 🔥 JSON API for Postman
@app.route("/api/predict", methods=["POST"])
def api_predict():

    data = request.get_json()

    inputs = [data.get(col, 0) for col in columns]

    prediction = model.predict([inputs])[0]

    return jsonify({
        "prediction": float(round(prediction, 3)),
        "status": "success"
    })


if __name__ == "__main__":
    app.run(debug=True)