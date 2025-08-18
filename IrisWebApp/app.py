from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd  

app = Flask(__name__)

# Load model, scaler, encoder
model_path = os.path.join(os.path.dirname(__file__), "iris_model.pkl") 
model = joblib.load(model_path) 

scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl") 
scaler = joblib.load(scaler_path) 

label_encoder_path = os.path.join(os.path.dirname(__file__), "label_encoder.pkl") 
label_encoder = joblib.load(label_encoder_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/flower')
def flower():
    return render_template('flower.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()   # <-- Read JSON from JS
    sl = float(data['sepal_length'])
    sw = float(data['sepal_width'])
    pl = float(data['petal_length'])
    pw = float(data['petal_width'])

    # Scale input using DataFrame (avoids sklearn warning)
    input_df = pd.DataFrame([[sl, sw, pl, pw]], 
                            columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
    scaled_features = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_features)[0]

    # Decode label (species name)
    species = label_encoder.inverse_transform([prediction])[0]

    # Return JSON to JS
    return jsonify({'prediction': species})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
