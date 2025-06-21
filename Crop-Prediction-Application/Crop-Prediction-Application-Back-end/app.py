from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import numpy as np
from PIL import Image
import tensorflow as tf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend on port 5173 to talk to this backend


# Config
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MODEL_PATH_TASK2 = 'models/final_Xception_model_task_2.keras'
MODEL_PATH_TASK1 = 'models/final_EfficientNetB0_model_task_1.keras'
MODEL_PATH_TASK3 = 'models/final_MobileNet_model_task_3.keras'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model once at startup
model_task2 = tf.keras.models.load_model(MODEL_PATH_TASK2)
model_task1 = tf.keras.models.load_model(MODEL_PATH_TASK1)
model_task3 = tf.keras.models.load_model(MODEL_PATH_TASK3)

# Class names (adjust these to match the dataset)
variety_names = [
    "ADT45",
    "AndraPonni",
    "AtchayaPonni",
    "IR20",
    "KarnatakaPonni",
    "Onthanel",
    "Ponni",
    "RR",
    "Surya",
    "Zonal"
]
label_names = [
    "bacterial_leaf_blight",
    "bacterial_leaf_streak",
    "bacterial_panicle_blight",
    "blast",
    "brown_spot",
    "dead_heart",
    "downy_mildew",
    "hispa",
    "normal",
    "tungro"
]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB')
    img = img.resize((224, 224))  # Adjust if your model uses a different input size
    img_array = np.array(img)   
    return np.expand_dims(img_array, axis=0)

@app.route('/predict-variety', methods=['POST'])
def predict_variety():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        # Preprocess and predict
        input_image = preprocess_image(image_path)
        predictions = model_task2.predict(input_image)
        predicted_variety = variety_names[np.argmax(predictions)]

        # Optional: delete the uploaded image
        os.remove(image_path)

        return jsonify({
            'prediction': predicted_variety
        })
    else:
        return jsonify({'error': 'Invalid file type'}), 400

@app.route('/predict-labels', methods=['POST'])
def predict_labels():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        # Preprocess and predict
        input_image = preprocess_image(image_path)
        predictions = model_task1.predict(input_image)
        predicted_label = label_names[np.argmax(predictions)]

        # Optional: delete the uploaded image
        os.remove(image_path)

        return jsonify({
            'prediction': predicted_label
        })
    else:
        return jsonify({'error': 'Invalid file type'}), 400
    
@app.route('/predict-age', methods=['POST'])
def predict_ages():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(image_path)

        # Preprocess and predict
        input_image = preprocess_image(image_path)
        predictions = model_task3.predict(input_image)
        predicted_ages = [int(round(age[0])) for age in predictions]# age is usually a regression output

        # Optional: delete the uploaded image
        os.remove(image_path)

        return jsonify({
            'prediction': predicted_ages
        })
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)