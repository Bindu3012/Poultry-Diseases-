from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model("poultry_model.h5")

class_names = [
    "Salmonella",
    "Newcastle",
    "Coccidiosis",
    "Healthy"
]

treatments = {
    "Salmonella": "Improve hygiene and isolate infected birds. Use antibiotics if prescribed.",
    "Newcastle": "Isolate birds immediately and vaccinate flock.",
    "Coccidiosis": "Administer anticoccidial drugs and maintain dry litter.",
    "Healthy": "No treatment required. Maintain proper hygiene."
}

@app.route("/")
def home():
    return "Poultry Disease API Running"

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    file = request.files["image"]
    image = Image.open(file).convert("RGB")
    image = image.resize((224, 224))

    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    confidence = float(np.max(prediction))

    disease = class_names[class_index]

    return jsonify({
        "disease": disease,
        "confidence": round(confidence, 2),
        "treatment": treatments[disease]
    })

if __name__ == "__main__":
  app.run(host="127.0.0.1", port=5000, debug=True)