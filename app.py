from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the .pkl file
with open('engine.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize the Flask app
app = Flask(__name__)

# Basic test route to check if Flask is working
@app.route('/')
def home():
    return "Flask is working!"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data as JSON
        data = request.json
        features = np.array([data['engine_rpm'], data['lub_oil_pressure'], data['fuel_pressure'],
                             data['coolant_pressure'], data['lub_oil_temp'], data['coolant_temp'],
                             data['temperature_difference']]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)
        confidence = model.predict_proba(features)[:, 1]

        return jsonify({
            "prediction": int(prediction[0]),
            "confidence": float(confidence[0])
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))  # Runs on localhost:5000
