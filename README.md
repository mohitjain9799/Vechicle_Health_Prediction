# Engine Health Prediction API

This project provides a RESTful API for predicting engine health based on various sensor readings. The API uses a pre-trained machine learning model stored in a `pickle` file (`engine.pkl`) to make predictions on input data.

## Project Structure

- `app.py`: Main Flask application file containing the API endpoints.
- `engine.pkl`: Pre-trained machine learning model for predictions.
- `requirements.txt`: Lists Python libraries needed to run the application.

## Requirements

- Python 3.x
- Flask
- Numpy
- Pickle (for model loading)


## Getting Started

Step 1: Clone the Repository

git clone https://github.com/your-username/engine-health-prediction-api.git
cd engine-health-prediction-api

Step 2: Install Dependencies
Install the required libraries:

pip install -r requirements.txt

Step 3: Add the Model File

Ensure the engine.pkl model file is in the root directory alongside app.py. This file should be a pre-trained model with predict and predict_proba methods.

Step 4: Run the Application

Start the Flask server:

python app.py
The application will run on http://localhost:5000 by default.

API Endpoints

1. Home

Endpoint: /

Method: GET

Description: A test endpoint to check if the API is running.

Example Request

curl http://localhost:5000/

Example Response

Flask is working!

2. Prediction

Endpoint: /predict

Method: POST

Description: Predicts engine health based on input sensor features.

Request Body: JSON format with the following fields:

engine_rpm: (float) Engine RPM

lub_oil_pressure: (float) Lubricant oil pressure

fuel_pressure: (float) Fuel pressure

coolant_pressure: (float) Coolant pressure

lub_oil_temp: (float) Lubricant oil temperature

coolant_temp: (float) Coolant temperature

temperature_difference: (float) Temperature difference

Example Request

curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{
    "engine_rpm": 3000,
    "lub_oil_pressure": 50,
    "fuel_pressure": 75,
    "coolant_pressure": 60,
    "lub_oil_temp": 80,
    "coolant_temp": 90,
    "temperature_difference": 10
}'

Example Response
{
  "prediction": 1,
  "confidence": 0.85
}

Project Resources

Flask Documentation: https://flask.palletsprojects.com/

NumPy Documentation: https://numpy.org/doc/

Contact:

For further questions or issues, please contact the project maintainer:

Name: Mohit Jain

Email: mohitjain9799@gmail.com
