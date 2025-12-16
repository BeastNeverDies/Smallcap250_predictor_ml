import joblib
import os

MODEL_PATH = os.path.join("ml", "model.pkl")


def load_model():
    """
    Loads trained ML model from disk.
    """

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Trained model not found at {MODEL_PATH}."
        )

    return joblib.load(MODEL_PATH)
