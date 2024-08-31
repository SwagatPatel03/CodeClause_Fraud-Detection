# Fraud Detection
This project aims to detect fraudulent transactions in a credit card dataset using machine learning. The model is built with Python, Pandas, and Scikit-learn, and the deployment is handled through a Flask web application with a user-friendly interface for uploading transaction data and receiving predictions.

The goal of this project is to detect potentially fraudulent credit card transactions by applying anomaly detection and classification algorithms. Given the highly imbalanced nature of the dataset, resampling techniques like SMOTE and careful feature scaling were employed.

## Technologies Used
Python: Main programming language.
Pandas: For data manipulation and analysis.
Scikit-learn: For building and training the machine learning model.
Flask: For deploying the model as a web application.
HTML/CSS: For creating a simple, user-friendly web interface.
Installation
Clone the repository:

## Copy code
git clone https://github.com/yourusername/credit-card-fraud-detection.git

## Dataset
The dataset used for this project contains transaction details from credit cards, including time, amount, and various anonymized features (V1, V2, ... V28). The target variable Class indicates whether a transaction is fraudulent (1) or legitimate (0).
Dataset Link : https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## Model Training
The model is trained using a Random Forest Classifier, with SMOTE applied to address class imbalance. The features Time and Amount were scaled using a Standard Scaler.

## Preprocessing Steps:
Scaling of Time and Amount to scaled_time and scaled_amount.
Oversampling the minority class (fraudulent transactions) using SMOTE.
Model:

## Random Forest Classifier
Trained on the scaled_time, scaled_amount, and V1 to V28 features.
#Deployment
The model is deployed using Flask as a web application. Users can enter the required transaction data, and the model will predict whether each transaction is fraudulent or legitimate.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.
