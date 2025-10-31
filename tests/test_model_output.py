import os
import pickle
import numpy as np




def test_model_prediction():
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
model_path = os.path.join(repo_root, "model.pkl")
assert os.path.exists(model_path), "model.pkl not found!"
with open(model_path, "rb") as f:
model, scaler = pickle.load(f)
sample = np.array([[1, 35, 5, 50000, 2, 1, 1, 60000]])
scaled = scaler.transform(sample)
pred = model.predict(scaled)
assert pred[0] in [0, 1], "Model prediction not binary!"
