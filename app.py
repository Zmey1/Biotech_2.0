from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load your model
with open('stacking_ensemble_model1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    input_data = request.json['inputData']

    # Preprocess input data as needed

    # Make prediction using your model
    prediction = model.predict([input_data])[0]  # Assuming your model expects a list of inputs

    # Return prediction as JSON response
    return jsonify({'prediction': str(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
