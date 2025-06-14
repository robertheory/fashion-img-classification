from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from flask_cors import CORS
import base64
import pickle
from schemas.classify import ImageClassificationResponse
from PIL import Image
import numpy as np
import io
import os

# API Info
info = Info(
    title="Fashion Classification API",
    version="1.0.0",
    description="Fashion Classification API for image classification tasks",
)

# Initialize Flask app with OpenAPI
app = OpenAPI(__name__, info=info)
CORS(app)

# API Tags
home_tag = Tag(
    name="Docs",
    description="Documentation selection: Swagger, Redoc or ReDoc"
)

classify_tag = Tag(
    name="Classify",
    description="Classify fashion images"
)


@app.get('/', tags=[home_tag])
def home():
    """Redirect to /openapi, screen that allows choosing the documentation style."""
    return redirect('/openapi/swagger')


def load_model(model_filename='fashion_image_classification_model.pkl'):
    """Carrega o modelo de ML usando pickle."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..', '..', 'ml', model_filename)
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found")
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model


def preprocess_image(image_bytes, size=(64, 64)):
    """Pré-processa a imagem para o formato esperado pelo modelo."""
    img = Image.open(io.BytesIO(image_bytes)).convert('L')  # grayscale
    img = img.resize(size)
    img_array = np.array(img).astype(np.float32) / 255.0
    img_array = img_array.flatten().reshape(1, -1)  # shape (1, 4096)
    return img_array


@app.post(
    '/classify',
    tags=[classify_tag],
    summary="Classify the uploaded fashion image",
    responses={"200": ImageClassificationResponse},
)
def classify():
    """
    Receives an image via multipart/form-data with the attribute name 'image'
    and converts it to base64. Loads a ML model using pickle.
    """
    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400

    image = request.files['image']
    image_bytes = image.read()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    image_base64 = f"data:image/jpeg;base64,{image_base64}"

    try:
        model = load_model()
    except FileNotFoundError as e:
        return {"error": str(e)}, 500

    img_array = preprocess_image(image_bytes)

    prediction = model.predict(img_array)

    print(f"Prediction: {prediction}")

    return {"prediction": prediction.tolist()}
