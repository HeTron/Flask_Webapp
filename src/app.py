from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
model_path = 'bitcoin_price_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    """Render the home page with the input form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Receive input features from the form and return the model prediction."""
    try:
        # Extract features from the form
        open_price = float(request.form['open'])
        high = float(request.form['high'])
        low = float(request.form['low'])
        price_lag1 = float(request.form['price_lag1'])
        price_7day_rolling_mean = float(request.form['price_7day_rolling_mean'])

        # Prepare the feature array for prediction
        features = np.array([[open_price, high, low, price_lag1, price_7day_rolling_mean]])

        # Make prediction
        prediction = model.predict(features)

        # Return the result
        return render_template('index.html', prediction_text=f'Predicted Bitcoin Price: ${prediction[0]:,.2f}')
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Error processing the request'}), 500

if __name__ == "__main__":
    app.run(debug=True)
