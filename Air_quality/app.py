from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model/air_quality_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the user
    try:
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        pm25 = float(request.form['pm25'])
        pm10 = float(request.form['pm10'])
        no2 = float(request.form['no2'])
        so2 = float(request.form['so2'])
        co = float(request.form['co'])
        proximity = float(request.form['proximity'])
        population = float(request.form['population'])

        # Prepare the input data for prediction
        input_data = np.array([[temperature, humidity, pm25, pm10, no2, so2, co, proximity, population]])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Render the result page with the prediction
        return render_template('result.html', prediction=prediction)
    
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)

