import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Path: ../final_tomato_model.keras (relative to app/build)
MODEL_PATH = "../final_tomato_model.keras"
model = load_model(MODEL_PATH)

IMG_SIZE = (224, 224)   # change if you used different size
CLASS_NAMES = ["healthy", "disease_1", "disease_2"]  # ← your real class names

def predict_tomato_disease(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0   # if you normalized in training

    preds = model.predict(img_array, verbose=0)
    pred_idx = np.argmax(preds[0])
    confidence = float(preds[0][pred_idx])

    return {
        "class": CLASS_NAMES[pred_idx],
        "confidence": confidence
    }