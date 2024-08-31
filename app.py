from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open('model/fraud_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract features from the form
        features = [float(x) for x in request.form.values()]
        features = np.array(features).reshape(1, -1)
        
        # Predict using the model
        prediction = model.predict(features)[0]
        
        if prediction == 1:
            result = "Fraudulent Transaction"
        else:
            result = "Legitimate Transaction"

        return render_template('index.html', prediction_text=result)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
