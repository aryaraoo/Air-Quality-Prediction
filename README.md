# Air Quality Prediction

## Overview
This project predicts air quality using aritificial intelligence and machine learning models and provides a user-friendly web interface using Flask. The system takes various air quality parameters as input and predicts pollution levels, helping users understand environmental conditions in their area.

## Features
- **Machine Learning Model**: Predicts air quality based on historical and real-time data.
- **Flask Web Application**: Interactive web interface for users.
- **Web UI**: Displays predictions.
- **Data Visualization**: Graphs and charts to illustrate air quality trends.
- **User-Friendly Design**: Responsive and easy to navigate.

## Tech Stack
- **Backend**: Flask, Python
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Visualization**: Matplotlib, Seaborn, Plotly

## Installation
### Prerequisites
Ensure you have Python installed (>=3.7). Install dependencies using:
```bash
pip install -r requirements.txt
```

### Running the Application
1. Clone the repository:
   ```bash
   https://github.com/aryaraoo/Air-Quality-Prediction
   ```
2. Navigate to the project directory:
   ```bash
   cd Air-Quality-Prediction
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and visit:
   ```
   
   ```

## Dataset
- The model is trained on an air quality dataset containing parameters like **PM2.5, PM10, CO, NO2, SO2,Kms from industrial place,Population Temperature, and Humidity**.
- Data preprocessing includes handling missing values, feature scaling, and normalization.

## Model Training
- **Algorithm**: Uses Random forest.
- **Training**: Implemented using Scikit-learn.
- **Evaluation**: Measures accuracy using RMSE, MAE, and R² score.

## Web Interface
- **Home Page**: Introduction and instructions.
- **Prediction Page**: Users input air quality parameters and get results.
- **Visualization Page**: Displays historical data trends.

## Future Enhancements
- Integrating real-time API data.
- Deploying on cloud platforms (AWS/GCP/Heroku).
- Adding more advanced ML models (Deep Learning).

## Contributors
- **Aryaraoo** (shivanirao539@gmail.com / aryaraoo)

## License
This project is licensed under the MIT License.

