
# Engine Health Prediction API

This API predicts engine health based on input sensor features using a pre-trained model. The application is built with Flask and can be set up quickly by following the steps below.

## Getting Started

### Step 1: Clone the Repository

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/mohitjain9799/Vechicle_Health_Prediction.git
cd Vechicle_Health_Prediction
```

### Step 2: Install Dependencies

Install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```

### Step 3: Add the Model File

Place the `engine.pkl` model file in the root directory alongside `app.py`. This file should be a pre-trained model with `predict` and `predict_proba` methods.

### Step 4: Run the Application

Start the Flask server:

```bash
python app.py
```

The application will run on [http://localhost:5000](http://localhost:5000) by default.

## API Endpoints

### Home

- **Endpoint:** `/`
- **Method:** `GET`
- **Description:** A test endpoint to check if the API is running.

**Example Request:**

```bash
curl http://localhost:5000/
```

**Example Response:**

```json
Flask is working!
```

### Prediction

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Description:** Predicts engine health based on input sensor features.

#### Request Body

The input should be in JSON format with the following fields:

- `engine_rpm`: (float) Engine RPM
- `lub_oil_pressure`: (float) Lubricant oil pressure
- `fuel_pressure`: (float) Fuel pressure
- `coolant_pressure`: (float) Coolant pressure
- `lub_oil_temp`: (float) Lubricant oil temperature
- `coolant_temp`: (float) Coolant temperature
- `temperature_difference`: (float) Temperature difference

**Example Request:**

```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{
  "engine_rpm": 3000,
  "lub_oil_pressure": 50,
  "fuel_pressure": 75,
  "coolant_pressure": 60,
  "lub_oil_temp": 80,
  "coolant_temp": 90,
  "temperature_difference": 10
}'
```

**Example Response:**

```json
{
  "prediction": 1,
  "confidence": 0.85
}
```

## Project Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [NumPy Documentation](https://numpy.org/doc/)

## Contact

For further questions or issues, please contact the project maintainer:

- **Name:** Mohit Jain
- **Email:** mohitjain9799@gmail.com
