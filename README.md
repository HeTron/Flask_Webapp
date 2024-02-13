## Bitcoin Price Prediction App

This repository contains a machine learning project aimed at predicting Bitcoin prices. 
The project utilizes historical Bitcoin price data to train a predictive model and deploys the model through a Streamlit web application for easy interaction and prediction.

### Project Structure

bitcoin_price_model.pkl: Serialized file of the trained machine learning model.
app.py: The main Python script that utilizes Streamlit to create a web application for interacting with the predictive model.
requirements.txt: A file listing all the Python libraries that the project depends on.

### Features
The model predicts Bitcoin prices based on the following features:

Open Price
High Price
Low Price
Price Lag1 (Price from the previous day)
Price 7-Day Rolling Mean

### Setup Instructions

To run this project locally, follow these steps:

### Clone the Repository:

git clone https://github.com/HeTron/Streamlit-app-project.git
cd Streamlit-app-project
### Create and Activate a Virtual Environment:

###### *For Unix/macOS:*
python3 -m venv .venv
source .venv/bin/activate

###### *For Windows:*
python -m venv .venv
.\.venv\Scripts\activate

### Install Required Libraries:

pip install -r requirements.txt

### Run the Streamlit App:

streamlit run app.py

### How to Use the App
After running the Streamlit app, navigate to the local URL provided by Streamlit (usually http://localhost:8501). Input the required features into the form and click the "Predict" button to see the Bitcoin price prediction.

### Model Information
The predictive model is a RandomForestRegressor trained on historical Bitcoin price data. It has been optimized for accuracy through hyperparameter tuning and validated using time-series cross-validation to ensure robustness.

### Contributing
We welcome contributions to improve the project! Please feel free to fork the repository, make your changes, and submit a pull request.

