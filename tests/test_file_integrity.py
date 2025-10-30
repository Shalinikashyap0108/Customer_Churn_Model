import os

def test_files_exist():
    required_files = ["churn_analysis.py", "app.py", "requirements.txt", "templates/index.html"]
    for file in required_files:
        assert os.path.exists(file), f"{file} is missing!"
