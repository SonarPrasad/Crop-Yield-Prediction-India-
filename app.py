from flask import Flask, render_template, request
from joblib import load

import pandas as pd

app = Flask(__name__)

# Load the saved Random Forest model
loaded_rf_model = load('notebook/model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        # Extract features from the form data
        crop = request.form['Crop']
        season = request.form['Season']
        state = request.form['State']
        area = float(request.form['Area'])
        production = float(request.form['Production'])
        annual_rainfall = float(request.form['Annual_Rainfall'])
        fertilizer = float(request.form['Fertilizer'])
        pesticide = float(request.form['Pesticide'])

        # Prepare the features as a single array
        features = [[crop, season, state, area, production, annual_rainfall, fertilizer, pesticide]]

        # Convert the features to a pandas DataFrame
        df = pd.DataFrame(features, columns=['Crop', 'Season', 'State', 'Area', 'Production', 'Annual_Rainfall', 'Fertilizer', 'Pesticide'])

        # Use the loaded Random Forest model to make a prediction
        prediction = loaded_rf_model.predict(df)
        prediction = round(prediction[0], 4)

        return render_template('result.html', prediction=prediction)
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)