import os
import subprocess

def test_model_training_runs():
    result = subprocess.run(["python", "churn_analysis.py"], capture_output=True)
    assert result.returncode == 0, "Model training script failed!"
    assert os.path.exists("model.pkl"), "Model file not created!"
