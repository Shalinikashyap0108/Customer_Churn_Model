import os
import subprocess




def test_model_training_runs():
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
result = subprocess.run([
"python",
"churn_analysis.py"
], cwd=repo_root, capture_output=True)


assert result.returncode == 0, (
"Model training script failed!\n"
f"stdout:\n{result.stdout.decode()}\n"
f"stderr:\n{result.stderr.decode()}"
)
assert os.path.exists(os.path.join(repo_root, "model.pkl")), "Model file not created!"
